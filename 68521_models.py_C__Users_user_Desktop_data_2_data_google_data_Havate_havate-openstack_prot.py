from django.db import models


CLUSTER_TYPE_UCSM_MANAGED = 'ucsm_m'
CLUSTER_TYPE_STANDALONE_C = 'stand_c'
CLUSTER_TYPE_CHOICES = (
    (CLUSTER_TYPE_UCSM_MANAGED, 'UCSM Managed'),
    (CLUSTER_TYPE_STANDALONE_C, 'Standalone c-Series')
)

OS_CLUSTER_TYPE_ALL_IN_ONE = 'all'
OS_CLUSTER_TYPE_CHOICES = (
    (OS_CLUSTER_TYPE_ALL_IN_ONE, 'All in One'),
)

OS_TYPE_UBUNTU = 'ubuntu'
OS_TYPE_CHOICES = (
    (OS_TYPE_UBUNTU, 'Ubuntu'),
)

class OpenstackSettings(models.Model):
    cluster_name = models.CharField(max_length=100, blank=True)
    cluster_type = models.CharField(max_length=20, choices=CLUSTER_TYPE_CHOICES, blank=True, default=CLUSTER_TYPE_UCSM_MANAGED)
    ucsm_hostname = models.CharField(verbose_name='UCSM IP Address / Hostname', max_length=100, blank=True)
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    os_cluster_type = models.CharField(max_length=20, choices=OS_CLUSTER_TYPE_CHOICES, blank=True, default=OS_CLUSTER_TYPE_ALL_IN_ONE)
    os_type = models.CharField(max_length=20, choices=OS_TYPE_CHOICES, blank=True, default=OS_TYPE_UBUNTU)
    mgmt_vlan = models.CharField(max_length=30, blank=True, default='12')
    pxe_vlan = models.CharField(max_length=30, blank=True, default='13')
    iscsi_vlan = models.CharField(max_length=30, blank=True)
    storage_vlan = models.CharField(max_length=30, blank=True)
    public_provider_vlan = models.CharField(max_length=30, blank=True)
    private_vlan = models.CharField(max_length=30, blank=True)
    tenants_vlan = models.CharField(max_length=30, blank=True, default='20-25')
    mgmt_subnet = models.CharField(max_length=30, blank=True, default='10.1.1.0/24')
    pxe_subnet = models.CharField(max_length=30, blank=True,  default='13.1.1.0/24')
    iscsi_subnet = models.CharField(max_length=30, blank=True)
    storage_subnet = models.CharField(max_length=30, blank=True)
    public_provider_subnet = models.CharField(max_length=30, blank=True)
    private_subnet = models.CharField(max_length=30, blank=True)
    tenants_subnet = models.CharField(max_length=30, blank=True)
    mac_pool = models.CharField(max_length=30, blank=True)
    mac_pool_size = models.CharField(max_length=30, blank=True)
    kvm_ip_pool = models.CharField(max_length=30, blank=True)
    kvm_ip_pool_size = models.CharField(max_length=30, blank=True)
    default_gateway = models.CharField(max_length=50, blank=True)
    subnet_mask = models.CharField(max_length=50, blank=True)
    dns = models.CharField(max_length=50, blank=True)
    hostname_prefix_compute_nodes = models.CharField(verbose_name='Compute Nodes', max_length=50, blank=True)
    hostname_prefix_swift_nodes = models.CharField(verbose_name='Swift Nodes', max_length=50, blank=True)


class NodeSettings(models.Model):
    node_name = models.CharField(max_length=200, blank=True)
    node_number = models.IntegerField()
    chassis_number = models.IntegerField()
    blade_number = models.IntegerField()
    aio = models.BooleanField()
    compute = models.BooleanField()
    network = models.BooleanField()
    swift = models.BooleanField()
    cinder = models.BooleanField()
    class Meta:
        ordering = ['node_number']


