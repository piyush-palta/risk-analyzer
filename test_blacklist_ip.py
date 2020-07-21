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
from risk_calculator.blacklist_ip import blacklistIP

"""
* Test Cases to test blacklistIP
* 
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class TestBlackListIP(unittest.TestCase):

    bl_list = blacklistIP('full_blacklist_database.txt')    
    
    #Test Cases are designed based on verification with the available blacklist database
    def testCase1(self):
        self.assertEqual(TestBlackListIP.bl_list.check('59.89.26.52'), 1)

    def testCase2(self):
        self.assertEqual(TestBlackListIP.bl_list.check('106.42.195.157'), 0)

    def testCase3(self):
        self.assertEqual(TestBlackListIP.bl_list.check('2403:6200:8000:a6:7514:7bd9:2998:e8bb'), 1)

    def testCase4(self):
        self.assertEqual(TestBlackListIP.bl_list.check('2402:6200:8000:a6:7514:7bd9:2998:e8bb'), 0)
