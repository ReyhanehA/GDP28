# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OpenstackSettings'
        db.create_table(u'config_openstacksettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cluster_name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cluster_type', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('ucsm_hostname', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('os_cluster_type', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('os_type', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('mgmt_vlan', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('pxe_vlan', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('iscsi_vlan', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('storage_vlan', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('public_provider_vlan', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('private_vlan', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('tenants_vlan', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('mgmt_subnet', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('pxe_subnet', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('iscsi_subnet', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('storage_subnet', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('public_provider_subnet', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('private_subnet', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('tenants_subnet', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('mac_pool', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('mac_pool_size', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('hostname_prefix_compute_nodes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('hostname_prefix_swift_nodes', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'config', ['OpenstackSettings'])

        # Adding model 'NodeSettings'
        db.create_table(u'config_nodesettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aio', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('compute', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('network', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('swift', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cinder', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'config', ['NodeSettings'])


    def backwards(self, orm):
        # Deleting model 'OpenstackSettings'
        db.delete_table(u'config_openstacksettings')

        # Deleting model 'NodeSettings'
        db.delete_table(u'config_nodesettings')


    models = {
        u'config.nodesettings': {
            'Meta': {'object_name': 'NodeSettings'},
            'aio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cinder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'compute': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'swift': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'config.openstacksettings': {
            'Meta': {'object_name': 'OpenstackSettings'},
            'cluster_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cluster_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'hostname_prefix_compute_nodes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'hostname_prefix_swift_nodes': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iscsi_subnet': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'iscsi_vlan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mac_pool': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mac_pool_size': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mgmt_subnet': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mgmt_vlan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'os_cluster_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'os_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'private_subnet': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'private_vlan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'public_provider_subnet': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'public_provider_vlan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'pxe_subnet': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'pxe_vlan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'storage_subnet': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'storage_vlan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'tenants_subnet': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'tenants_vlan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ucsm_hostname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['config']