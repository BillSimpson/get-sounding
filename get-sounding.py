#
# A simple python script to pull down a sounding text file from 
# U. Wyoming's website.
#
import sys
import os
import datetime

if len(sys.argv) < 2:
    print ('usage: give a date argument as YYYY-MM-DD-HH where HH is 00 or 12')
    print ('  Time is in UTC = Zulu = Z timezone')
    print ('  an optional argument is the station name STNM (a five-digit number)')
    exit (1)

# set the date
try:
    dt = datetime.datetime.strptime(sys.argv[1],'%Y-%m-%d-%H')
    print(dt)
except:
    print ('could not parse date')
    exit(1)

# set the STNM string (location) -- get from UWyo website
try:
    STNM_str = sys.argv[2]
except:   # default to Fairbanks (PAFA) = 70261
    STNM_str = '70261'


scriptpre = 'curl \'http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&'
year = dt.strftime('%Y')
month = dt.strftime('%m')
day = dt.strftime('%d')
hour = dt.strftime('%H')
scriptdate = 'YEAR='+year+'&MONTH='+month+'&FROM='+day+hour+'&TO='+day+hour
scriptloc = '&STNM='+STNM_str+'\' --output sounding-'+STNM_str+'-'
filename = dt.strftime('%Y-%m-%d-%H.txt')

os.system(scriptpre+scriptdate+scriptloc+filename)
