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


"""
* Rule Engine has predefined set of rules to evaluate an IP address and assign
* a risk score based on that
*
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class ruleEngine: 
    """ Create new instance
        @param ip_addr : the IP address to be evaluated
        Constructor assigns IP as attribute and initiates Risk Calculation
     """
    
    def __init__(self, ip_addr):
        self.ip_addr=ip_addr
        self.calculateScore()

    def calculateScore(self):
        #Hard coding the values for now, rules to inserted here
        self.score="35"
