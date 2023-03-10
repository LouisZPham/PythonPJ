'''Import the required modules - datetime and playsound.
Get the desired alarm time from the user as input in the format HH:MM:SS.
Extract the hour, minute, seconds, and period (AM or PM) from the user's input.
Print a message to indicate that the alarm is being set up.
Enter into an infinite loop that repeatedly checks the current time and compares it with the desired alarm time.
Get the current time by using the datetime module.
Extract the current hour, minute, seconds, and period (AM or PM) from the current time.
Check if the alarm period matches the current period.
Check if the alarm hour matches the current hour.
Check if the alarm minute matches the current minute.
Check if the alarm seconds matches the current seconds.
If all of the above conditions are true, play the alarm sound using the playsound module and print a "Wake Up!" message.
Exit the loop using the break statement.
'''

from datetime import datetime   
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break