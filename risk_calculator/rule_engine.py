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

from risk_calculator.DataBases import ruleDB

"""
* Rule Engine has predefined set of rules to evaluate an IP address and assign
* a risk score based on that
*
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class ruleEngine: 
    """ Create new instance
        @param ip_addr : the IP address to be evaluated
        @param userID : the userID that is being accessed
        Constructor assigns IP as attribute and initiates Risk Calculation
     """
    
    def __init__(self):
        self.db = ruleDB.database()            
        
    def init_eval(self):
        self.rule1()

    #Check if IP address is in Whitelist and matches with userID
    def rule1(self):
        if(self.db.checkWhitelist(self.ip_addr,self.userID)):
            #Each failed attempt adds 2 to risk score & 7 every 5th attempt
            self.score += (2*(self.attempts)   + 5*(self.attempts//5))
        else :
            self.rule2()
        self.rule4()

    # Check if IP address matches with user ID similar to current ID using Fuzzy Logic &
    # edit distance concept and subsidizes failed attempts penalty 
    def rule2(self):
        if(self.db.fuzzyMatchUserID(self.ip_addr,self.userID)):
            #Each failed attempt adds 4 to the risk score & 8 every 5th attempt 
            self.score +=  (4*(self.attempts)  + 4*(self.attempts//5))
        else:
            self.rule3()

    # Since IP Address &  User ID combination doesn't exist in Database, user will now be treated
    # as a foreign entity 
    def rule3(self):
        #Each failed attempt adds 5 to the risk score & every 5th attempt adds 10
        self.score += (5*(self.attempts)  + 5*(self.attempts//5))
    
    # Checks if there are other IP accesses for this userID
    def rule4(self):
        user_attempts = self.db.checkUserIDAttempts(self.userID)
        # Each adds a score of 9
        self.score  += 9*(user_attempts)
        

    def getScore(self, ip_addr, userID):
        self.ip_addr = ip_addr
        self.userID = userID
        self.attempts = self.db.getNumberofFailedAttempts(self.ip_addr)
        self.score = 0
        self.init_eval()
        return self.score
