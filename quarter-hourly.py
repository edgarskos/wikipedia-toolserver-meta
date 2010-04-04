#!/usr/bin/python 
import datetime
import time 
import MySQLdb

import sys
sys.path.append( '/home/hroest/')
sys.path.append( '/home/hroest/scripts/')
import create_flagged_data
import replag_lib

today = datetime.date.today()
now = datetime.datetime.now()
this_year = today.year
this_month = today.month

db = MySQLdb.connect(read_default_file="/home/hroest/.my.cnf")

###########################################################################
logfile = open('/home/hroest/quarter-hourly.log', 'a')
logfile.write( '\nrun started:\n')
logfile.write( '\tstart time %s\n' % now)

replag_lib.insert_db( db )
logfile.write( '\tinserted row into db' )

now = datetime.datetime.now()
logfile.write( '\tend time %s\n' % now)
logfile.close()