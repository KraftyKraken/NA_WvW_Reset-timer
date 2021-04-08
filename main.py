# 2nd draft of reset countdown timer.

# grab yer imports
import dateutil.relativedelta as rel
import datetime
import time
from tkinter import *

# creating window and name it.
root = Tk()
root.geometry("180x120")
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
    # find today and today in UTC, set up temp
    temp = 0
    today_utc = datetime.datetime.utcnow()

    # Find when next friday (for US), i.e., reset is.
    reset_utc = rel.relativedelta(hour=2, minute=0, second=0, microsecond=0, days=1, weekday=rel.SA)
    reset = today_utc + reset_utc
    
    # give in seconds to work with below. This should ignore DT and ST now.
    time_until = int((reset-today_utc).total_seconds())

    try:
        temp = time_until
    except:
        print("Incorrect values! Date Calculation malfunction")
    while temp > -1:

        # minutes=temp/60, seconds = temp%60)
        minutes, seconds = divmod(temp, 60)

        # hours. Pop up hours only if we've got a full hour.
        # hours = temp/60, minutes = temp%60)
        hours = 0
        if minutes > 60:
            hours, minutes = divmod(minutes, 60)

        # format to 2 decimal places every time for niceness
        hour.set("{0:3d}".format(hours))
        minute.set("{0:2d}".format(minutes))
        second.set("{0:2d}".format(seconds))

        # Try to update the counter. Vague because if user closes, it's an exception, but that's ok.
        try:
            root.update()
            time.sleep(1)
            temp -= 1
        except:
            return 0


btn = Button(root, text='How Long Until Reset? ', bd='5', command=countdown)
btn.place(x=20, y=60)

root.mainloop()
