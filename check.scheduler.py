#!/usr/bin/python

'''
Author: Luke Simmons (VGR IT)
Date: 2015-10-05
Description: Monitor a dbms_scheduler job
Version: 1.0
'''

import cx_Oracle
import re
import sys

# Insert your username/password here
username=""
password=""

# Insert the name of your job here
job_name = ""

sql = "SELECT status FROM (SELECT * FROM USER_SCHEDULER_JOB_LOG where job_name='" + job_name + "' ORDER BY log_date desc) WHERE ROWNUM=1"

db = cx_Oracle.connect(username, password);
cursor = db.cursor()
cursor.execute(sql)
row = cursor.fetchone()
failed = re.match( r'FAILED', row[0])
if failed:
	print job_name + " - FAILED"
	sys.exit(2)
succeed = re.match( r'SUCCEEDED', row[0])
if succeeded:
	print job_name + " - SUCCEEDED"
	sys.exit(0)

print "UKNOWN STATUS"
sys.exit(2)
