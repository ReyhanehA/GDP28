#!/usr/bin/python
from UcsSdk import *

# This script will sync the organisation between two UCS Manager.
# Scenario:
# Both UCS Manager contains organisation "TestSyncOrg" under org-root.
# However UCS Manager with handle2 contains service profile "TestSyncSP" under "TestSyncOrg" but no servie profile under UCS Manager with handle1.
#
# Goal is to make both the Organisation same i.e. to copy the service profile from handle2 to handle1.

handle1_ip = '0.0.0.0'
handle1_user = 'username'
handle1_password = 'password'

handle2_ip = '0.0.0.0'
handle2_user = 'username'
handle2_password = 'password'

try:

    
    handle1 = UcsHandle()
    handle1.Login(handle1_ip, handle1_user, handle1_password)
    
    handle2 = UcsHandle()
    handle2.Login(handle2_ip, handle2_user, handle2_password)
    
    
    moList1 = handle1.GetManagedObject(None, OrgOrg.ClassId(), {OrgOrg.DN:"org-root/org-TestSyncOrg"}, YesOrNo.TRUE)
    moList2 = handle2.GetManagedObject(None, OrgOrg.ClassId(), {OrgOrg.DN:"org-root/org-TestSyncOrg"}, YesOrNo.TRUE)
 
	# Compare will return a different object either showing sign "=>" means managed object has to be added to reference object 
	# or  sign "<=" means # managed object has to be removed from reference object.
    modiff = CompareManagedObject(referenceObject=moList1, differenceObject=moList2)
    print "\n modiff"
    WriteObject(modiff)

	# Run the sync object on the reference object handle. In this case, handle1.
    handle1.SyncManagedObject(difference=modiff1, deleteNotPresent=True, dumpXml=False)
    
    handle1.Logout()
    handle2.Logout()
    
except Exception, err:
    handle1.Logout()
    handle2.Logout()
    print "Exception:", str(err)
    import traceback, sys
    print '-'*60
    traceback.print_exc(file=sys.stdout)    
    print '-'*60
    
    
