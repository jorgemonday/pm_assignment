# -*- coding: utf-8 -*-

# -----------------------------------------------------------
# This program opens the w_data (5).dat file located in the same directory, and outputs the day number with the
# smallest spread between the MnT column (lowest temperature of the day) and the MxT column (highest temperature of the day).
#
# This program expects a file formatted a follows -
# File encoding: us-ascii
# Column 3:  1 or 2 digit numerical day number in a range from 1 to 31
# Column 6:  5 character maximum temperature field, with optional negative first character, optional asterisk denoting monthly high
# Column 13: 5 character minimum temperature field, with optional negative first character, optional asterisk denoting monthly low
#
# Original assignment text:
# In the attached file (w_data.dat), you’ll find daily weather data.   Download this text file, then write a program to output the 
# day number (column one) with the smallest temperature spread (the maximum temperature is the second column, 
# the minimum the third column).
#
# Jorge Rosas
# December 9, 2019
# -----------------------------------------------------------

import io

# These variables will hold the final result
result_day = None
result_spread = None

try :
    # open the file in read only mode
    with io.open('w_data (5).dat', mode='r', encoding='us-ascii') as weather_file :                 
        
        lines = [line.rstrip('\n') for line in weather_file]     
        
        for line in lines :
            
            if len(line) > 20 : # aproximately 20 characters needed to contain the necessary data in a line
                
                try :
                    day_of_month = int(line[0:5].strip()) # if not a valid data record, it will fail and move on to the next line.                    
                    day_low_temp = int(line[12:17].replace('*','').strip())
                    day_high_temp = int(line[6:11].replace('*','').strip())
                    day_temp_spread = day_high_temp - day_low_temp

                    if not result_spread :
                        result_spread = day_temp_spread
                        result_day = day_of_month
                        
                    else :
                        # compare and declare a new winner if this is a lower spread value
                        if day_temp_spread < result_spread : 
                            result_spread = day_temp_spread
                            result_day = day_of_month

                except ValueError : # not a valid line for this application
                    continue

    # compute finished, display the day of the month with lowest spread and quit.
    print(str(result_day))
    quit()

except IOError :
    print ('Could not read the weather file, program exiting')
    quit()