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

import ipaddress
from risk_calculator.DataBases import sqliteDB

"""
* Module to check if the IP is already blacklisted i.e. , by checking it's presence
* in popular IP blacklist dumps and return the highest possible Risk Score if found
* 
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class blacklistIP:
    """ Create new instance
        @param bldata_file : the location of file containing blacklist IPs data 
        Constructor assigns IP as attribute and initiates search in blacklist dumps
     """
    def __init__(self, bldata_file = 'full_blacklist_database.txt'):
        self.bldata_file = bldata_file
        self.db = sqliteDB.database()
        self.init_db()        

    def init_db(self):
        self.db.create_table()
        f = open(self.bldata_file)
        file_data=f.readlines()
        ipv4 = []
        ipv6 = []
        
        for line in file_data:
            #this is based on the structure of the blacklist data file used
            ip_addr = str(line.split('\t',1)[0])
            if('.' in ip_addr):
                ip_hash = hashIPv4(ip_addr)
                ipv4.append(ip_hash)
            else :
                ip_hash1,ip_hash2 = hashIPv6(ip_addr)
                ipv6.append([ip_hash1,ip_hash2])

        #Intialize database by extracting data from file to db            
        self.db.insertManyIPv4(ipv4)
        self.db.insertManyIPv6(ipv6)
        
  
    def check(self, ip_addr):
        if('.' in ip_addr):
            ip_hash = hashIPv4(ip_addr)
            return self.db.searchIPv4(ip_hash)
        else:
            ip_hash1, ip_hash2 = hashIPv6(ip_addr)
            return self.db.searchIPv6(ip_hash1, ip_hash2)

""" Hashes IPv6 addresses
    @param ip_addr : IPv6 address to be hashed
    return {hash1, hash2} : Returns two 64-bit hash numbers
"""
def hashIPv6(ip_addr):
    ip_addr = str(ipaddress.ip_address(ip_addr).exploded)
    ip = ip_addr.split(':')
    ip = [int(i,16) for i in ip]
    hash1=0
    for i in range(4):
        hash1 += (ip[i]*( 1<<(16*(3-i))))
    hash2=0
    for i in range(4):
        hash2 += (ip[i+4]*( 1<<(16*(3-i))))
    if hash1 >= (1<<63):
        hash1-=(1<<64)
    if hash2 >= (1<<63):
        hash2-=(1<<64)
    return {hash1, hash2}


""" Generates IPv6 address from the hash number 
    @param hash1 : 64-bit first part of the IPv6 hash
    @param hash2 : 64-bit second part of the IPv6 hash 
    return ip_addr : Return IPv6 address
"""
def getIPv6(hash1, hash2):
    ip = []
    for i in range(4):
        ip.append(hash2%(1<<16))
        hash2//=(1<<16)
    for i in range(4):
        ip.append(hash1%(1<<16))
        hash1//=(1<<16)
    ip = ip[::-1]
    ip = [str(hex(i)[2:]) for i in ip]
    ip_addr = str(ipaddress.ip_address(':'.join(ip)))
    return ip_addr     


"""Function : Hashes IPv4 addresses
    @param ip_addr : IPv4 address to be hashed
    return hashNum : Returns a 32-bit hash number
"""
def hashIPv4(ip_addr):
    ip = ip_addr.split('.')
    ip = [int(i) for i in ip]
    hashNum=0
    for i in range(4):
        hashNum += (ip[i]*( 1<<(8*(3-i))))
    return hashNum


""" Generates IPv4 address from the hash number 
    @param hashNum : 32-bit hash number
    return ip_addr : Return IPv4 address
"""
def getIPv4(hashNum):
    ip = []
    for i in range(4):
        ip.append(hashNum%(1<<8))
        hashNum//=(1<<8)
    ip = ip[::-1]
    ip = [str(i) for i in ip]
    ip_addr = '.'.join(ip)
    return ip_addr
