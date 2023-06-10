# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2012 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.template.defaultfilters import title  # noqa
from django.utils.translation import ugettext_lazy as _  # noqa

from horizon import tables


def pretty_service_names(name):
    name = name.replace('-', ' ')
    if name in ['ec2', 's3']:
        name = name.upper()
    else:
        name = title(name)
    return name


class DownloadEC2(tables.LinkAction):
    name = "download_ec2"
    verbose_name = _("Download EC2 Credentials")
    verbose_name_plural = _("Download EC2 Credentials")
    classes = ("btn-download",)
    url = "horizon:project:access_and_security:api_access:ec2"


class DownloadOpenRC(tables.LinkAction):
    name = "download_openrc"
    verbose_name = _("Download OpenStack RC File")
    verbose_name_plural = _("Download OpenStack RC File")
    classes = ("btn-download",)
    url = "horizon:project:access_and_security:api_access:openrc"


class EndpointsTable(tables.DataTable):
    api_name = tables.Column('type',
                             verbose_name=_("Service"),
                             filters=(pretty_service_names,))
    api_endpoint = tables.Column('public_url',
                                 verbose_name=_("Service Endpoint"))

    class Meta:
        name = "endpoints"
        verbose_name = _("API Endpoints")
        multi_select = False
        table_actions = (DownloadOpenRC, DownloadEC2,)
