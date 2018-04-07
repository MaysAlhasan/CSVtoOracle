# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 16:09:45 2018

@author: maysa
"""

import csv
import cx_Oracle

with open("Sample_data.csv", "r") as f:
  reader = csv.reader(f)
  mylist = list(reader)
connect_string = "sys/sys@ORCL"
con = cx_Oracle.connect(connect_string,mode=cx_Oracle.SYSDBA)

cur=con.cursor()

cur.executemany("INSERT INTO SampleData VALUES(:1,:2,:3)",mylist[1:][:])

con.commit ()
cur.close()
con.close()