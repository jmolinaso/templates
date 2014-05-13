#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import os
import argparse
import logging

class DBPostgres:
    """Class to connect to a postgreSQL and register to recieve notifications
    """
    connection = None
    arguments = None
    logger = logging.getLogger()

    def connect(self,host,dbname,user,password):
        """Method to stablish connection towards the database
        Usage: DBConnect.connect(host,database,user,password)
        """
        try:
            self.logger.debug("Getting connected to {}".format(self.arguments.database))
            self.connection = psycopg2.connect(host=host,dbname=dbname,user=user,password=password)
            self.logger.debug("Successfully connected")

        except psycopg2.DatabaseError, e:
            self.logger.error('Error %s' % e)


    def disconnect(self):
        """Method to disconnect from the database
        """
        self.logger.debug("Disconnecting from {}".format(self.arguments.database))
        
        if self.connection:
            self.connection.close()

    def execsql(self,query,data=None,register=False):
        """Method to interact with the database:
        (*) if we pass data as tuples then we will proceed with an insert with the values
        (*) if register is set to True,it will receive changes when something changes in the table.
        """
        self.logger.debug("Excuting query %s",query)
            
        if register:
            pass
            
        if data is not None:
            if self.connection:
                try:
                    cursor = self.connection.cursor()
                    cursor.executeSQL(query)
                    ret = cursor.fetchall
                    print ret
                except psycopg2.DatabaseError, e:
                    self.logger.error('Error %s' % e)

        elif query:
            pass

    def upload_data(self,table,data):
        sqlinsert_stmt = "insert into " + table + "("
        self.execsql(query=sqlinsert_stmt)

    def run(self, *args):
        """Excute the class for testing purposes
        """
        if __name__ == '__main__':
            parser = argparse.ArgumentParser(description="Module to connect and get updates from PostgreSQL")
            parser.add_argument("-v","--debug",help="Display the debug messages", action="store_true")
            parser.add_argument("-i","--interactive",help="Enter in interactive mode to execute some SQL and wait for events",action="store_true")
            parser.add_argument("-u","--username", help="Username to connect to the postgreSQL")
            parser.add_argument("-p","--password", help="Password to connect to the postgreSQL")
            parser.add_argument("-s","--server", help="Hostname of the postgreSQL")
            parser.add_argument("-d","--database", help="Database name to connect")
            self.arguments = parser.parse_args()
            if self.arguments.debug:
                logging.basicConfig(format='%(asctime)s [%(levelname)s] [%(module)s::%(funcName)s] %(message)s', level=logging.DEBUG)
            else:
                logging.basicConfig(format='%(asctime)s [%(levelname)s] [%(module)s::%(funcName)s] %(message)s', level=logging.INFO)
            
            self.logger.info("Starting %s",__file__)
            self.logger.info("Requesting connection to database %s",self.arguments.database)
            self.connect(self.arguments.server,self.arguments.database,self.arguments.username,self.arguments.password)
            if self.arguments.interactive:
                self.interactive()
            self.logger.info("End %s",__file__)
            self.disconnect()

    def interactive(self):
        self.logger.info("Entered in interactive mode")
        imsg = raw_input('# ')
        self.logger.info("Input [%s]",imsg)
        while imsg <> 'exit':
            imsg = raw_input('# ')
            self.logger.info("Input [%s]",imsg)
        self.logger.info("Exit from interactive mode")

if __name__ == '__main__':
    db = DBPostgres()
    db.run()
