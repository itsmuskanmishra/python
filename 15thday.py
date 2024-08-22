import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
hour=int(input("Enter time:"))
print("hour")

if (hour>=0 and hour<12):
    print("Good morning!")
elif (hour>=12 and hour<17):
    print("Good afternoon sir!")
elif (hour>=17 and hour<24):
    print("Good night!")
    
