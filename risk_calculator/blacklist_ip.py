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

import pydnsbl 


"""
* Module to check if the IP is already blacklisted i.e. , by checking it's presence
* in popular IP blacklist dumps and return the highest possible Risk Score if found
* 
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class blacklistIP:
    """ Create new instance
        @param ip_addr : the IP address to be evaluated
        Constructor assigns IP as attribute and initiates search in blacklist dumps
     """
    def __init__(self, ip_addr):
        self.ip_addr=ip_addr
        self.searchBlackLists()

    def searchBlackLists(self):
        ip_checker = pydnsbl.DNSBLIpChecker()
        result = ip_checker.check(self.ip_addr)
        self.blacklist = result.blacklisted 
