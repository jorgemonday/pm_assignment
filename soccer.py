# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# This program opens the soccer.dat file located in the same directory, and outputs the name of the team with the 
# smallest difference between the 'for' and 'against' goals. 
# 
# This program expects a file formatted a follows -
# File encoding: us-ascii
# Column 8: 15 character max string respresenting the team name
# Column 44: 1 to 3 digit number representing the number of goals scored by the team
# Column 51: 1 to 3 digit number representing the number of goals scored against the team
#
# Original assignment text:
# The attached soccer.dat file contains the results from the English Premier League.  The columns labeled ‘F’ and ‘A’ contain the 
# total number of goals scored for and against each team in that season (so Arsenal scored 79 goals against opponents, and had 
# 36 goals scored against them). Write a program to print the name of the team with the smallest difference in ‘for’ 
# and ‘against’ goals.
#
# Jorge Rosas
# December 9, 2019
# -----------------------------------------------------------

import io
import sys

# require a minimum version of python to guarantee compatability
MIN_PYTHON = (2, 7)
if sys.version_info < MIN_PYTHON:
    sys.exit("Sorry, Python %s.%s or later is required.\n" % MIN_PYTHON)

# These variables will hold the final result
result_team = None
result_spread = None

try :
    # open the file in read only mode
    with io.open('soccer.dat', mode='r', encoding='us-ascii') as soccer_file :                 
        
        lines = [line.rstrip('\n') for line in soccer_file]     
        
        for line in lines :
            
            if len(line) > 53 : # number of characters needed to contain the necessary data in a record
                
                try :
                    team_name = line[7:21].strip() # if not a valid data record, it will fail and move on to the next line.                    
                    goals_for = int(line[43:46].strip())
                    goals_against = int(line[50:53].strip())
                    goal_spread = goals_for - goals_against

                    if goal_spread < 0 :
                        goal_spread = goal_spread * -1 # flip to positive if the team had a higher number of goals against them.

                    if not result_spread :
                        result_spread = goal_spread
                        result_team = team_name                        
                    else :
                        # compare and declare a new winner if this is a lower spread value
                        if goal_spread < result_spread : 
                            result_spread = goal_spread
                            result_team = team_name

                except ValueError : # not a valid line for this application
                    continue

    # compute finished, display the day of the month with lowest spread and quit.
    print(str(result_team))
    quit()

except IOError :
    print ('Could not read the soccer file, program exiting')
    quit()