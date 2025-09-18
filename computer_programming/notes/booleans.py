#BHR 2nd Boolean Notes

import time as time
import datetime as date

over = False

print(over)

name = "Ms. LaRose"

print(name.isupper())

print(bool(name))

current_time = time.time()
readable_time = time.ctime(current_time)
now = date.datetime.now()
current_hour = now.strftime("%H")
# Month %m month number or %b or %B
#Day = %d
#year = %Y full %y two digit
#hour = %H
# Minutes %M
#Seconds = %S

print(f"Current time in second since January 1, 1970(epoch time): {current_time}\nCurrent Time: {readable_time}\nCurrent time according to datetime: {now}\nHour: {current_hour*66}\nMy hour variable is a string: {isinstance(current_hour, str)}\nMy hour variable is a integer: {isinstance(current_hour, int)}\nMy hour variable is a float: {isinstance(current_hour, float)}\nMy hour variable is a boolean: {isinstance(current_hour, bool)}")