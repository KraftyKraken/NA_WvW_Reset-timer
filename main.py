# prime of reset cntd

# grab yer imports
import dateutil.relativedelta as rel
import datetime
import time
from datetime import date
from tkinter import *

# creating window and name it.
root = Tk()
root.geometry("200x120")
root.title("GW2 - CD")

# def time vars
hour = StringVar()
hour.set("0")
minute = StringVar()
minute.set("0")
second = StringVar()
second.set("0")


# create the boxes. I should disallow input there, but maybe later.
hourEntry = Entry(root, width=3, font=("Arial", 14, ""), textvariable=hour)
hourEntry.place(x=20, y=20)
minuteEntry = Entry(root, width=3, font=("Arial", 14, ""), textvariable=minute)
minuteEntry.place(x=70, y=20)
secondEntry = Entry(root, width=3, font=("Arial", 14, ""), textvariable=second)
secondEntry.place(x=120, y=20)


def countdown():
    # find today and today in UTC
    today = date.today()
    today_UTC = datetime.datetime.utcnow()
    
    # Find when next friday, i.e., reset is.
    fri = rel.relativedelta(days=1, weekday=rel.FR)
    friday = today + fri
    
    # convert to utc and give in seconds. This should ignore DT and ST now.
    friday_utc = rel.relativedelta(hours=26) + friday
    time_until = int((friday_utc-today_UTC).total_seconds())

    try:
        temp = time_until
    except:
        print("Incorrect values! Date Calculation malfunction")
    while temp > -1:

        # minutes=temp/60, seconds = temp%60)
        mins, secs = divmod(temp, 60)

        # hours. Pop up hours only if we've got a full hour.
        # hours = temp/60, minutes = temp%60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        # format to 2 decimal places every time for niceness
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # Try to update the counter. Vague because if user closes, it's an exception, but that's ok.
        try:
            root.update()
            time.sleep(1)
            temp -= 1
        except:
            return 0


btn = Button(root, text='How long until reset?', bd='5', command=countdown)
btn.place(x=30, y=70)

root.mainloop()
