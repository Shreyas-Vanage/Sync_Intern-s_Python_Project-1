# Alarm Clock using Python

from tkinter import *
import datetime
import time
import winsound

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

def alarm():
    #Loop running
    while True:
        # For Settin Alarm
        set_alarm = f"{hour.get()}:{minute.get()}:{second.get()}"
 
        # Waiting for 1 seconds
        time.sleep(1)
 
        # Getting current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
 
        # Checking whether set alarm is equal to current time or not
        if current_time == set_alarm:
            print("Time to Wake up")
            # Playing sound for alarm
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)


clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
 
# Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
 
#The Time required to set the alarm clock is
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)
 
#Code for taking the time input by user
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)
 
clock.mainloop()
#Now the execution of the window

# Importing Required Library for Code
from tkinter import *
import datetime
import time
import winsound
from threading import *
 
# Creating Object
root = Tk()
 
# Setting geometry code
root.geometry("400x200")
 
# Using Threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()
 
def alarm():
    # Looping (Infinite)
    while True:
        # Set Alarm
        set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
 
        # Waiting for 1 seconds
        time.sleep(1)
 
        # Code for getting current time 
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,set_alarm_time)
 
        # Checking whether set alarm is equal to current time or not
        if current_time == set_alarm_time:
            print("Time to Wake up")
            # Playing sound
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
 
# Adding Labels, Frames, Buttons, Option menus
Label(root,text="Alarm Clock",font=("Helvetica 20 bold"),fg="red").pack(pady=10)
Label(root,text="Set Time",font=("Helvetica 15 bold")).pack()
 
frame = Frame(root)
frame.pack()
 
hour = StringVar(root)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24'
        )
hour.set(hours[0])
 
hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)
 
minute = StringVar(root)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
minute.set(minutes[0])
 
mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)
 
second = StringVar(root)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59', '60')
second.set(seconds[0])
 
secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
 
Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)
 
# Executing Tkinter
root.mainloop()
