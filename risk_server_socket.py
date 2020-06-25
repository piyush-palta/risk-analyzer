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

import socket
import sys

"""
* Socket for Risk Analyzer Server, creates & open socket to enable communication with client
* 
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""



class riskServerSocket:
    
    """ Create new instance
        @param host : the IP address of the host
        @param port : the port to open socket connection on
        Constructor creates & binds the socket & initiates connection with client
     """

    def __init__(self, host, port):
        self.host=host
        self.port=port
        self.sock = self.create_socket()
        self.bind_socket()
        self.start()


    #Creates socket instance   
    def create_socket(self):
        try:
            return socket.socket()
        except socket.error as msg:
            print("Socket creation error: " + str(msg))
        
    #Binds the socket and start listening for connections
    def bind_socket(self):
        try :
            print("Binding the port " + str(self.port))
            self.sock.bind((self.host,self.port));       
            self.sock.listen(5)
        except socket.error as msg:
            print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
            self.bind()

    #Establish connection with a client
    def start(self):
        self.conn, self.client_address = self.sock.accept()
        print("Connection established : " + "IP " + self.client_address[0] + " | Port " + str(self.client_address[1]))

    # Receive message from client
    def receive(self):
        while True:
            client_response = str(self.conn.recv(1024).decode("utf-8"))
            if(len(client_response)>0):
                self.msg = client_response
                self.ip_addr = self.msg
                break

    #Send message to client
    def send(self, msg):
        self.conn.send(str.encode(msg))
        self.conn.close()
        self.start()

    #Close socket connection
    def close(self):
        self.sock.close()