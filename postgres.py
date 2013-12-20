#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import os
import argparse


class DBPostgress:
	"""Class to connect to a postgreSQL and register to recieve notifications
	"""
	connection = None
	arguments = None

	def connect(self,host,dbname,user,password):
    	"""Method to stablish connection towards the database
    	Usage: DBConnect.connect(host,database,user,password)
    	"""
    	try:
      		if self.arguments.debug:
        		print "Getting connected to {}".format(self.arguments.database)
      		self.connection = psycopg2.connect(host=host,dbname=dbname,user=user,password=password)
      		if self.arguments.debug:
        		print "Successfully connected"
      
    	except psycopg2.DatabaseError, e:
      		print 'Error %s' % e
      

	def disconnect(self):
		"""Method to disconnect from the database
      	"""
      	if self.arguments.debug:
        	print "Disconnecting from {}".format(self.arguments.database)

      	if self.connection:
        	self.connection.close()

  	def execsql(self,query,register=False):
      	"""Method to query the database, if register is set to True
      	it will receive changes when something changes in the table
      	"""
      	if self.arguments.debug:
        	print "Excuting query "
      
      	if register:
        	pass

      	if self.connection:
        	try:
          		cursor = self.connection.cursor()
        		cursor.executeSQL(query)
          		ret = cursor.fetchall
          		print ret
        	except psycopg2.DatabaseError, e:
          		print 'Error %s' % e

  	def run(self, *args):
    	"""Excute the class for testing purposes
    	"""
    	parser = argparse.ArgumentParser(description="Module to connect and get updates from PostgreSQL")
    	parser.add_argument("-d","--debug",help="Display the debug messages", action="store_true")
    	parser.add_argument("-i","--interactive",help="Enter in interactive mode to execute some SQL and wait for events",action="store_true")
    	parser.add_argument("username", help="Username to connect to the postgreSQL")
    	parser.add_argument("password", help="Password to connect to the postgreSQL")
    	parser.add_argument("hostname", help="Hostname of the postgreSQL")
    	parser.add_argument("database", help="Database name to connect")
    	self.arguments = parser.parse_args()
    	self.connect(self.arguments.hostname,self.arguments.database,self.arguments.username,self.arguments.password)
    	self.disconnect()


if __name__ == '__main__':
  	db = DBPostgress()
  	db.run()
