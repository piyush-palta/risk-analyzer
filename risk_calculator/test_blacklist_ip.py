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
from blacklist_ip import blacklistIP

"""
* Test Cases to test blacklistIP
* 
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class TestBlackListIP(unittest.TestCase):
    
    #Test Cases are designed based on verification with online blacklist dumps
    def testCase1(self):
        self.assertEqual(blacklistIP('68.128.213.240').blacklist, True)

    def testCase2(self):
        self.assertEqual(blacklistIP('192.168.54.43').blacklist, True)

    def testCase3(self):
        self.assertEqual(blacklistIP('157.39.46.250').blacklist, True)

    def testCase4(self):
        self.assertEqual(blacklistIP('192.39.46.250').blacklist, False)
