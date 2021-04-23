# 6th draft of reset countdown timer.
# By: KraftyKraken - octonink@gmail.com
# Created: 4/7/2021

import dateutil.relativedelta as rel
import datetime
from tkinter import *
from tkinter import messagebox


# creating window and name it.
root = Tk()
root.geometry("200x140")
root.title("Reset Countdown")
try:
    root.iconbitmap(default='icon.ico')
except:
    messagebox.showerror("Icon Error", "Unable to find icon resource. Put me back with my friends!")
    exit(1)

# def time vars + other
hour = StringVar()
hour.set("0")
minute = StringVar()
minute.set("0")
second = StringVar()
second.set("0")
running = True

# create the boxes.
hourEntry = Entry(root, width=4, font=("Arial", 14, ""), textvariable=hour)
hourEntry.place(x=20, y=20)
minuteEntry = Entry(root, width=4, font=("Arial", 14, ""), textvariable=minute)
minuteEntry.place(x=77, y=20)
secondEntry = Entry(root, width=4, font=("Arial", 14, ""), textvariable=second)
secondEntry.place(x=133, y=20)


def na_time():
    # finds all the time calculations for na
    # restart if we're stopped.
    global running
    running = True

    today_utc = datetime.datetime.utcnow()

    # if today is not sat (sat 2am UTC when reset is)
    # find next saturday and say how long it is
    if today_utc.weekday() != 5:
        reset_utc = rel.relativedelta(hour=2, minute=0, second=0, microsecond=0, days=1, weekday=rel.SA)
        reset = today_utc + reset_utc
        countdown(int((reset-today_utc).total_seconds()))
    # today is saturday
    else:
        # we're after 2am in the day just go about it normally
        if datetime.datetime.utcnow().time() >= datetime.time(2, 0, 0, 0):
            reset_utc = rel.relativedelta(hour=2, minute=0, second=0, microsecond=0, days=1, weekday=rel.SA)
            reset = today_utc + reset_utc
            countdown(int((reset-today_utc).total_seconds()))
        # otherwise don't go to any other day, just give the 2hr countdown
        else:
            reset = today_utc + rel.relativedelta(hour=2, minute=0, second=0, microsecond=0)
            countdown(int((reset-today_utc).total_seconds()))


def my_raid():
    # finds custom time of today, set military time style
    # restart if we're stopped.
    global running
    running = True
    # Try to test cast all values to int
    try:
        int(hour.get())
        int(minute.get())
        int(second.get())
    except:
        messagebox.showerror("Bad Input", "Please input numbers into the boxes")
        return
    now = datetime.datetime.today()
    target_time = rel.relativedelta(hour=int(hour.get()), minute=int(minute.get()),
                                    second=int(minute.get()), microsecond=0)
    my_time = now + target_time
    if int((my_time-now).total_seconds()) <= 0:
        messagebox.showerror("Bad Input", "Please use military time\nFor PM, simply add 12 hour.")
    countdown(int((my_time-now).total_seconds()))


def countdown(work_time):
    # counts down the actual work
    temp = 0
    try:
        temp = work_time
    except:
        messagebox.showerror("Value Error", "Incorrect values! Date Calculation malfunction")
    while temp > -1:

        # minutes=temp/60, seconds = temp%60)
        minutes, seconds = divmod(temp, 60)

        # hours. Pop up hours only if we've got a full hour.
        # hours = temp/60, minutes = temp%60)
        hours = 0
        if minutes > 60:
            hours, minutes = divmod(minutes, 60)

        hour.set("{0:3d}".format(hours))
        minute.set("{0:2d}".format(minutes))
        second.set("{0:2d}".format(seconds))

        # Try to update output and countdown.
        try:
            if running:
                root.update()
                root.after(1000)
                temp -= 1
            else:
                temp = -1
                hour.set("0")
                minute.set("0")
                second.set("0")
                root.update()
        except:
            return 0


def close_program():
    response = messagebox.askyesno("Reset Countdown - Close?", "Do you want to close the program?")
    if response == 1:
        root.destroy()
    else:
        reply = messagebox.askokcancel("Reset Countdown - Accuracy", "Program was paused. "
                                                                     "Timing is now off. Press ok "
                                                                     "to re-enter desired time. Cancel to continue.")
        if reply == 1:
            stop_program()


def stop_program():
    global running
    running = False


btn = Button(root, text="NA? ", bd='5', command=na_time)
btn.place(x=20, y=60)
btn = Button(root, text="Custom Today", bd='5', command=my_raid)
btn.place(x=20, y=95)

# menu bar
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Reset", command=stop_program)
file_menu.add_separator()
file_menu.add_command(label="Close", command=close_program)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()
