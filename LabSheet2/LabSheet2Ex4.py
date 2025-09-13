index=1
LeastSleepNight=24
LeastSleepNightDate="0"
while index<=30:
    CurrentDate=str(input("Enter today's date in the format YY/MM/DD: "))
    CurrentNightHours=float(input("Enter today's amount of sleep: "))
    index+=1
    if CurrentNightHours < LeastSleepNight:
        LeastSleepNight=CurrentNightHours
        LeastSleepNightDate=CurrentDate
print("Night with least amount amount of",LeastSleepNight,"hours was on the",LeastSleepNightDate)        