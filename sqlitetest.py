#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('djinn_tables_v0.db')
print "Opened database successfully";

conn.execute('''CREATE TABLE USERS
       (ID INT PRIMARY KEY     NOT NULL,
       FIRST_NAME     TEXT    NOT NULL,
       LAST_NAME      TEXT    NOT NULL,
       EMAIL		  TEXT    NOT NULL,
       NO_TEAMS       INT     NOT NULL);''')


print "Table created successfully";

conn.close()