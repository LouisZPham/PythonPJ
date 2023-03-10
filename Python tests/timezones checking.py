import pytz
from datetime import datetime, timedelta

# create a list of time zones to check
time_zones = [pytz.timezone('Etc/GMT+{}'.format(i)) for i in range(-7, 8)]

# get the current datetime in UTC timezone
now_utc = datetime.utcnow()

# loop through each time zone and print the current date and time
for tz in time_zones:
    now_tz = now_utc.astimezone(tz)
    print('Time zone:', tz.zone)
    print('Current date and time:', now_tz.strftime('%Y-%m-%d %H:%M:%S %Z'))