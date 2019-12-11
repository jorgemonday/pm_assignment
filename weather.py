# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# This program opens the w_data (5).dat file located in the same directory,
# and outputs the day number with the smallest spread between the MnT column
# (lowest temperature of the day) and the MxT column (highest temperature
# of the day).
#
# This program expects a file formatted a follows -
# File encoding: us-ascii
# Column 3:  1 or 2 digit numerical day number in a range from 1 to 31
# Column 6:  5 character max temperature field, with optional negative first
#            character, optional asterisk denoting monthly high
# Column 13: 5 character minimum temperature field, with optional negative
#            first character, optional asterisk denoting monthly low
#
# Original assignment text:
# In the attached file (w_data.dat), you’ll find daily weather data.
# Download this text file, then write a program to output the day number
# (column one) with the smallest temperature spread (the maximum
# temperature is the second column, the minimum the third column).
#
#
# Jorge Rosas
# https://github.com/jorgemonday
# -----------------------------------------------------------

import io
import sys

# Application constants
MIN_PYTHON_VERSION = (2, 7)
DATA_FILE_NAME = 'w_data (5).dat'
RECORD_MINIMUM_NUM_CHARACTERS = 20  # If less, not a valid record
RECORD_START_POSITION_DAY = 0
RECORD_END_POSITION_DAY = 5
RECORD_START_POSITION_LOW_TEMP = 12
RECORD_END_POSITION_LOW_TEMP = 17
RECORD_START_POSITION_HIGH_TEMP = 6
RECORD_END_POSITION_HIGH_TEMP = 11

# Require a minimum version of python to guarantee compatability
if sys.version_info < MIN_PYTHON_VERSION:
    sys.exit("Sorry, Python %s.%s or later is required.\n" %
             MIN_PYTHON_VERSION)

# These variables will hold the final result
result_day = None
result_spread = None


try:
    # open the file in read only mode
    with io.open(DATA_FILE_NAME,
                 mode='r', encoding='us-ascii') as weather_file:

        lines = [line.rstrip('\n') for line in weather_file]

        for line in lines:

            if len(line) > RECORD_MINIMUM_NUM_CHARACTERS:

                # if not a valid data record, fail and move to the next line.
                try:
                    day_of_month = int(line[RECORD_START_POSITION_DAY:
                                            RECORD_END_POSITION_DAY].strip())
                    day_low_temp = int(line[RECORD_START_POSITION_LOW_TEMP:
                                            RECORD_END_POSITION_LOW_TEMP].
                                       replace('*', '').strip())
                    day_high_temp = int(line[RECORD_START_POSITION_HIGH_TEMP:
                                             RECORD_END_POSITION_HIGH_TEMP].
                                        replace('*', '').strip())
                    day_temp_spread = day_high_temp - day_low_temp

                    if not result_spread:
                        result_spread = day_temp_spread
                        result_day = day_of_month
                    else:
                        # compare and set a new value if this is a lower spread
                        if day_temp_spread < result_spread:
                            result_spread = day_temp_spread
                            result_day = day_of_month

                except ValueError:  # not a valid line for this application
                    continue

    # compute finished, display day of the month with lowest spread and quit.
    print(str(result_day))
    quit()

except IOError:
    print('Could not read the weather file, program exiting')
    quit()
