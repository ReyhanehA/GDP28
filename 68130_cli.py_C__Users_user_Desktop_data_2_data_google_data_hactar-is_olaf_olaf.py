# -*- coding: utf-8 -*-

"""
    Olaf
    ~~~~~~~~~~~~~
    command line tool to help you manage multiple requirements files.
"""

from __future__ import absolute_import
import glob
import click
import subprocess
import collections


@click.command()
@click.option('--prefix', '-p', default='requirements',
              help='Match files on {prefix}*.txt')
@click.option('--write', '-w', is_flag=True,
              help='Use if you want to commit the changes to your files.')
@click.argument('cmd', default='freeze', required=True)
def main(cmd, prefix, write):
    if cmd == 'freeze':
        freeze(prefix, write)
    if cmd == 'dupes':
        dupes(prefix, write)


def freeze(prefix, write):
    frozen = pipfreeze()
    files = create_files_store(prefix)
    unreqed = []

    match_versions(frozen, files, unreqed)
    add_installed(files, unreqed)
    find_duplicates(files)
    do_write(files, write)

    check_uninstalled(frozen, files)


def get_reqs_files(prefix):
    return glob.glob('{}*.txt'.format(prefix))


def create_files_store(prefix):
    files = []

    for name in get_reqs_files(prefix):
        files.append({
            'name': name,
            'packages': jam(name),
            'updated': [],
            'removed': []
        })

    return files


def dupes(prefix, write):
    files = create_files_store(prefix)
    find_duplicates(files)
    do_write(files, write)


def find_duplicates(files):

    primary = files[0]
    others = files[1:len(files)]

    for package in primary['packages'].copy():
        for other in others:
            otherpacks = other['packages']
            try:
                dupe = otherpacks[package]
            except KeyError:
                pass
            else:
                this = {
                    'file': primary['name'],
                    'package': package,
                    'version': primary['packages'][package]
                }
                that = {
                    'file': other['name'],
                    'package': package,
                    'version': other['packages'][package]
                }
                click.echo(
                    "Found {} in {} and {}".format(
                        package, this['file'], that['file']))
                value = click.prompt(
                    """[0]Keep both\n[1] Keep {} in {}\n[2] Keep {} in {}\n""".format(
                        this['version'],
                        this['file'],
                        that['version'],
                        that['file']),
                    type=int
                )
                if value == 1:
                    del otherpacks[package]
                    other['updated'].append(package)
                    other['removed'].append(package)
                elif value == 2:
                    del primary['packages'][package]
                    primary['updated'].append(package)
                    primary['removed'].append(package)


def write_updates(files):
    # write the requirements files.
    for req in files:
        if len(req['updated']) > 0:
            rewrite(req)
        else:
            click.echo('No updates in {}'.format(req['name']))


def print_updates(files):
    # print the requirements files.
    for req in files:
        output(req)


def match_versions(frozen, files, unreqed):
    for package, version in frozen:
        found = False
        for req in files:
            if package in req['packages']:
                if req['packages'][package] != version:
                    click.echo(
                        '{} specifies version {} of {}, the installed version is {}'.format(
                            req['name'], req['packages'][package], package, version))
                    value = click.prompt(
                        """[1] Update {}\n[2] Keep existing value\n""".format(req['name']),
                        type=int
                    )
                    if value == 1:
                        req['packages'][package] = version
                        req['updated'].append(package)
                    elif value == 2:
                        pass
                found = True

        if found is False:
            unreqed.append({
                package: version
            })


def check_uninstalled(frozen, files):
    installed = []
    reqed = []
    for k, v in frozen:
        installed.append(str(k))
    for reqs in files:
        for k, v in reqs['packages'].items():
            reqed.append(str(k))

    uninstalled = list(set(reqed) - set(installed))
    if len(uninstalled) > 0:
        click.echo(
            click.style(
                "The following packages are in your requirements but not installed.",
                fg='red'))
        click.echo(click.style('\n'.join(uninstalled), fg='red'))
    return uninstalled


def add_installed(files, unreqed):
    unique = [dict(y) for y in set(tuple(x.items()) for x in unreqed)]
    for package_d in unique:
        for package, version in package_d.items():
            # import pdb; pdb.set_trace()
            click.echo(
                u'{} is installed but not in any requirements file'.format(
                    package))
            pstr = '[0] Ignore\n'
            for index, rf in enumerate(files):
                pstr += '[{}] Add to {}\n'.format(index + 1, rf['name'])
            value = click.prompt(pstr, type=int)
            try:
                req_file = files[value - 1]
            except IndexError:
                click.echo('Not a valid selection soz.')
            else:
                req_file['packages'][package] = version
                req_file['updated'].append(package)


def pipfreeze():
    frozen = []
    try:
        packages = subprocess.check_output(["pip", "freeze"]).decode("utf-8")
    except subprocess.CalledProcessError as e:
        click.echo('Error with pip freeze: {}'.format(e))
    else:
        for line in packages.splitlines():
            sline = str(line)
            if sline.startswith(u'-e '):
                package, version = (sline.strip(), '')
                frozen.append((package, version))
            elif sline.startswith(u'## FIXME:'):
                pass
            elif u'==' in sline:
                package, version = sline.strip().split(u'==')
                frozen.append((package, version))

        return frozen


def jam(filename):
    packages = {}
    try:
        with open(filename, 'r') as infile:
            infile.seek(0)
            for line in infile.readlines():
                if line.startswith(u'-e '):
                    package, version = (line.strip(), '')
                    packages[package] = version
                elif '==' in line:
                    package, version = line.strip().split(u'==')
                    packages[package] = version
                else:
                    packages[line.strip()] = 'latest'

    except IOError:
        click.echo('File {} not found.'.format(filename))

    infile.close()
    return packages


def rewrite(req):
    try:
        with open(req['name'], 'w') as outfile:
            outfile.seek(0)
            outfile.truncate()
            packages = collections.OrderedDict(
                sorted(req['packages'].items(), key=lambda t: str(t[0]))
            )
            for k, v in packages.items():
                outfile.write('{}\n'.format(lineout(str(k), str(v))))
    except IOError:
        click.echo('File {} not found.'.format(req['name']))

    outfile.close()
    click.echo('Updated {} with packages \n\t{}'.format(
        req['name'], '\n\t'.join([str(_) for _ in req['updated']])))
    for item in req['removed']:
        click.echo(click.style('# Removed package {}'.format(item), fg='yellow'))


def output(req):
    click.echo('\n')
    click.echo('#' * 80)
    click.echo('# {}'.format(req['name']))
    click.echo('#' * 80)
    packages = collections.OrderedDict(
        sorted(req['packages'].items(), key=lambda t: str(t[0]))
    )
    for k, v in packages.items():
        if k not in req['updated']:
            click.echo(lineout(str(k), str(v)))
        else:
            click.echo(click.style(lineout(str(k), str(v)), fg='green'))

    for item in req['removed']:
        click.echo(click.style('# Removed package {}'.format(item), fg='yellow'))

    click.echo('\n')


def do_write(files, write):
    if write is True:
        write_updates(files)
    else:
        print_updates(files)


def lineout(package, version):
    if package.startswith(u'-e ') or version == u'latest':
        return package
    else:
        return '{}=={}'.format(package, version)
