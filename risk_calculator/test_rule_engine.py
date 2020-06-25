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
from rule_engine import ruleEngine

"""
* Test Cases for ruleEngine
* 
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""


class TestRuleEngine(unittest.TestCase):

    #Test Cases are designed based on dry run risk calculation of the IP address
    def testCase1(self):
        self.assertEqual(ruleEngine('68.128.213.240').score, '35')

    def testCase2(self):
        self.assertEqual(ruleEngine('192.168.54.43').score, '35')

    def testCase3(self):
        self.assertEqual(ruleEngine('157.39.46.250').score, '35')

    def testCase4(self):
        self.assertEqual(ruleEngine('192.39.46.250').score, '35')
