#!/usr/bin/python
from UcsSdk import *

# This script restores the UCS Manager to earlier state using stored backup.
# ImportUcsBackup(path=None, merge=False, dumpXml=False)
#
# Note : Make sure the backup file should exist before executing the script.

if __name__ == "__main__":
	try:
		handle = UcsHandle()
		handle.Login("0.0.0.0", "username", "password")
		
		BackupFilePath = r"C:\Backups\configlogical.xml"
		handle.ImportUcsBackup(path = BackupFilePath)

		handle.Logout()

	except Exception, err:
		handle.Logout()
		print "Exception:", str(err)
		import traceback, sys
		print '-'*60
		traceback.print_exc(file=sys.stdout)
		print '-'*60

