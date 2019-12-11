# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# This program opens the soccer.dat file located in the same directory,
# and outputs the name of the team with the smallest difference
# between the 'for' and 'against' goals.
#
# This program expects a file formatted a follows -
# File encoding: us-ascii
# Column 8: 15 character max string respresenting the team name
# Column 44: 3 digit number representing number of goals scored by team
# Column 51: 3 digit number representing number of goals scored against team
#
# Original assignment text:
# The attached soccer.dat file contains the results from the English Premier
# League.  The columns labeled ‘F’ and ‘A’ contain the total number of goals
# scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program
# to print the name of the team with the smallest difference in ‘for’
# and ‘against’ goals.
#
# Jorge Rosas
# https://github.com/jorgemonday
# -----------------------------------------------------------

import io
import sys

# Application constants
MIN_PYTHON_VERSION = (2, 7)
DATA_FILE_NAME = 'soccer.dat'
RECORD_MINIMUM_NUM_CHARACTERS = 53  # If less, not a valid record
RECORD_START_POSITION_TEAM_NAME = 7
RECORD_END_POSITION_TEAM_NAME = 21
RECORD_START_POSITION_GOALS_FOR = 43
RECORD_END_POSITION_GOALS_FOR = 46
RECORD_START_POSITION_GOALS_AGAINST = 50
RECORD_END_POSITION_GOALS_AGAINST = 53

# Require a minimum version of python to guarantee compatability
if sys.version_info < MIN_PYTHON_VERSION:
    sys.exit("Sorry, Python %s.%s or later is required.\n" %
             MIN_PYTHON_VERSION)

# These variables will hold the final result
result_team = None
result_spread = None

try:
    # open the file in read only mode
    with io.open(DATA_FILE_NAME, mode='r', encoding='us-ascii') as soccer_file:

        lines = [line.rstrip('\n') for line in soccer_file]

        for line in lines:

            if len(line) > RECORD_MINIMUM_NUM_CHARACTERS:

                # if not a valid data record, will fail and move to next line.
                try:
                    team_name = line[RECORD_START_POSITION_TEAM_NAME:
                                     RECORD_END_POSITION_TEAM_NAME].strip()
                    goals_for = int(line[RECORD_START_POSITION_GOALS_FOR:
                                         RECORD_END_POSITION_GOALS_FOR]
                                    .strip())
                    goals_against = int(line[
                                        RECORD_START_POSITION_GOALS_AGAINST:
                                        RECORD_END_POSITION_GOALS_AGAINST]
                                        .strip())
                    goal_spread = goals_for - goals_against

                    # a spread is always a positive number
                    if goal_spread < 0:
                        goal_spread = goal_spread * -1

                    if not result_spread:
                        result_spread = goal_spread
                        result_team = team_name
                    else:
                        # compare and set a new value if this is a lower spread
                        if goal_spread < result_spread:
                            result_spread = goal_spread
                            result_team = team_name

                except ValueError:  # not a valid line for this application
                    continue

    # compute finished, display the team with the lowest spread and quit.
    print(str(result_team))
    quit()

except IOError:
    print('Could not read the soccer file, program exiting')
    quit()
