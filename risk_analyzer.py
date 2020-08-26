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


from risk_server_socket import riskServerSocket
from risk_calculator import rule_engine as re, blacklist_ip as bls

"""
* Risk Analyzer is a standalone module and provides a black box interface to  
* calculate risk posed by an IP & can be invoked by merely providing the host IP 
* address and interfacing port number 
*
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class riskAnalyzer:
    
    def __init__(self, host, port):
        self.host=host
        self.port=port
        self.serverSocket = riskServerSocket(self.host, self.port)
        self.blacklistDB_init()
        self.ruleEngine_init()
        try:
            while True:
                self.serverSocket.receive()
                risk = self.calculateRisk()
                self.serverSocket.send(risk)
        except (IOError, SystemExit):
            raise
        except KeyboardInterrupt:
            self.serverSocket.close()
            print("Crtl+C Pressed. Shutting down.")

    def blacklistDB_init(self):
        self.blacklistDB = bls.blacklistIP('full_blacklist_database.txt')
    
    def ruleEngine_init(self):
        self.ruleEngine = re.ruleEngine()

    def calculateRisk(self):
        print(self.serverSocket.ip_addr)
        if(self.blacklistDB.check(self.serverSocket.ip_addr)):
            return "100"
        else:
            score = self.ruleEngine.getScore(self.serverSocket.ip_addr, self.serverSocket.userID)
            return score
        
