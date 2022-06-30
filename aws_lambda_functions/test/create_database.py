import sys
import logging
import pymysql
import json
import pymysql.cursors
import boto3
import collections
from datetime import datetime
import time

rds_host = "database-1-mariadb.cyuon3k4skgo.us-east-1.rds.amazonaws.com" 

username="admin"
password="12345678"
dbname="phpmyadmin"
dbport= 3306
try:
    conn= pymysql.connect (rds_host,user=username, passwd=password, port= dbport, connect_timeout=5)

except pymysql.MySQLError as e:
    print (e)
    sys.exit()

with conn.cursor() as cur:
	cur.execute("create database mariadb-javigr-celma")