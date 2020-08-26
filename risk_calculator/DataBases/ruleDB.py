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

import sqlite3
import numpy as np

"""
* ruleDB works as backend for rule_engine and stores all login events in
* a table with fields namely ip_addr, userID, event_success, event_time
* class < database > provides an interface to use this db
*
* @author < a href = "mailto:piyush.palta@outlook.com" > Piyush Palta < /a >
"""

class database:
    """sqlite3 database class that holds login attempts with timestamp """
   
    def __init__(self, db_location = ':memory:'):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(db_location)
        self.cur = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """create database tables"""
        self.cur.execute('''CREATE TABLE login(ip_addr text, userID text, event_time timestamp, event_success bool)''')

    def insertEvent(self,ip_addr,userID,event_time,event_success):
        """insert a row of data to current cursor in login table"""
        self.cur.execute('INSERT INTO login VALUES(?,?,?,?)', (ip_addr,userID,event_time,event_success))
          
    def insertManyEvents(self, event_list):
        """insert bulk data to the table in one go"""
        self.cur.executemany('INSERT INTO login VALUES(?,?,?,?)', [(i[0], i[1], i[2], i[3]) for i in event_list])

    def getNumberofFailedAttempts(self, ip_addr):
        self.cur.execute("SELECT COUNT(*) FROM login WHERE event_success=0 AND ip_addr = (?)", (ip_addr,))
        data=self.cur.fetchone()
        if data is None:
            return 0
        return data[0]
        
    def checkWhitelist(self,ip_addr,userID):
        self.cur.execute("SELECT * FROM login WHERE event_success=1 AND ip_addr = (?) AND userID=(?)", (ip_addr,userID))
        data=self.cur.fetchone()
        if data is None:
            return 0
        return 1

    def checkUserIDAttempts(self, userID):
        self.cur.execute("SELECT COUNT(DISTINCT ip_addr) FROM login WHERE event_success=0 AND userID = (?)", (userID,))
        data=self.cur.fetchone()
        if data is None:
            return 0
        return data[0]

    def fuzzyMatchUserID(self, ip_addr, userID):
        """fuzzy matches userID with ip_addr in the table"""
        self.cur.execute("SELECT userID FROM login WHERE event_success=1 AND ip_addr = (?)", (ip_addr,))
        data=self.cur.fetchall()
        for id in data:
            if(levenshtein_ratio_and_distance(userID, id)>0.9):
                return 1
        return 0


    def close(self):
        """close sqlite3 connection"""
        self.connection.close()


def levenshtein_ratio_and_distance(s, t, ratio_calc = True):
    """ levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        # print(distance) 
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return distance[row][col]