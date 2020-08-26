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

import unittest
from risk_analyzer import riskAnalyzer
import socket

"""
* Unit Testing of riskAnalyzer as a whole
* 
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

# host and port are based on riskAnalyzer server
host = '127.0.0.1'
port = 1342

client_socket1 = socket.socket()
client_socket1.connect((host, port))

client_socket2 = socket.socket()
client_socket2.connect((host, port))

client_socket3 = socket.socket()
client_socket3.connect((host, port))

client_socket4 = socket.socket()
client_socket4.connect((host, port))



#   Each test case here opens up a socket and asserts based on the risk score received

class TestRiskAnalyzer(unittest.TestCase):
        
    def testCase1(self):
        client_socket1.send(str.encode('1.2.167.196-elytron'))
        while True:
        	data = client_socket1.recv(1024).decode("utf-8")
	        if (len(data) > 0):
		        self.assertEqual(data,'100')
		        break
        client_socket1.close()
        
    def testCase2(self):
        client_socket2.send(str.encode('103.214.219.250-user1'))
        while True:
        	data = client_socket2.recv(1024).decode("utf-8")
	        if (len(data) > 0):
		        self.assertEqual(data, '100')
		        break
        client_socket2.close()

    def testCase3(self):     
        client_socket3.send(str.encode('192.39.46.250-user'))
        while True:
        	data = client_socket3.recv(1024).decode("utf-8")
	        if (len(data) > 0):
		        self.assertEqual(data, '0')
		        break
        client_socket3.close()

    def testCase4(self):
        client_socket4.send(str.encode('157.39.46.250-user'))
        while True:
        	data = client_socket4.recv(1024).decode("utf-8")
	        if (len(data) > 0):
		        self.assertEqual(data, '0')
		        break
        client_socket4.close()        
