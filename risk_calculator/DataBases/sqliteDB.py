"""
* JBoss, Home of Professional Open Source.
* Copyright 2020 Red Hat, Inc., and individual contributors
* as indicated by the @author tags.
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http: // www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
"""

import sqlite3

"""
* sqliteDB works as backend for blacklist_IP and stores all blacklisted IPs in
* two tables namely IPv4 and IPv6
* class < database > provides an interface to use sqlite3 db
*
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class database:
    """sqlite3 database class that holds blacklisted IPs"""
   
    def __init__(self, db_location = ':memory:'):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(db_location)
        self.cur = self.connection.cursor()

    def create_table(self):
        """create database tables IPv4 and IPv6"""
        self.cur.execute('''CREATE TABLE IPv4(ip_hash integer)''')
        self.cur.execute('''CREATE TABLE IPv6(ip_hash1 integer, ip_hash2 integer)''')

    def insertIPv4(self, val):
        """insert a row of data to current cursor in IPv4 table"""
        self.cur.execute('INSERT INTO IPv4 VALUES(?)', (val,))
          
    def insertManyIPv4(self, ip_list):
        """insert bulk data to the database in one go"""        
        self.cur.executemany("INSERT INTO IPv4 VALUES(?)", [(i,) for i in ip_list])

    def insertIPv6(self, val1, val2):
        """insert a row of data to current cursor in IPv6 table"""
        self.cur.execute('INSERT INTO IPv6 VALUES(?,?)', (val1,val2))

    def insertManyIPv6(self, ip_list):
        """insert bulk data to the database in one go"""
        self.cur.executemany("INSERT INTO IPv6 VALUES(?,?)", [(i[0], i[1]) for i in ip_list])

    def searchIPv4(self, ip_hash):
        """searches if given ip_hash exists in the table"""
        self.cur.execute("SELECT * FROM IPv4 WHERE ip_hash = ?", (ip_hash,))
        data=self.cur.fetchone()
        if data is None:
            return 0
        return 1

    def searchIPv6(self, ip_hash1, ip_hash2):
        """searches if given ip hash combination exists in the table"""
        self.cur.execute("SELECT * FROM IPv6 WHERE ip_hash1 = (?) AND ip_hash2 = (?) ", (ip_hash1,ip_hash2))
        data=self.cur.fetchone()
        if data is None:
            return 0
        return 1

    def close(self):
        """close sqlite3 connection"""
        self.connection.close()