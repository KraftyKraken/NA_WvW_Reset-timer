# 7th draft of reset countdown timer.
# By: KraftyKraken - octonink@gmail.com
# Created: 4/7/2021

import _tkinter
import dateutil.relativedelta as rel
import datetime
import winsound
import time
import threading
from tkinter import *
from tkinter import messagebox


# creating window and name it.
root = Tk()
root.geometry("200x140")
root.title("Reset Countdown")
try:
    root.iconbitmap(default='icon.ico')
except _tkinter.TclError:
    messagebox.showerror("Icon Error", "Unable to find icon resource. Put me back with my friends!")
    exit(1)

# Vars that need to be shared around to work.
hour = StringVar()
hour.set("0")
minute = StringVar()
minute.set("0")
second = StringVar()
second.set("0")
thirty_min = BooleanVar()
thirty_min.set(False)
five_min = BooleanVar()
five_min.set(False)
running = BooleanVar()
running.set(True)
temp = 0

# create the boxes.
hourEntry = Entry(root, width=4, font=("Arial", 14, ""), textvariable=hour)
hourEntry.place(x=20, y=20)
minuteEntry = Entry(root, width=4, font=("Arial", 14, ""), textvariable=minute)
minuteEntry.place(x=77, y=20)
secondEntry = Entry(root, width=4, font=("Arial", 14, ""), textvariable=second)
secondEntry.place(x=133, y=20)


def na_time():
    running.set(True)
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


def eu_time():
    running.set(True)
    today_utc = datetime.datetime.utcnow()

    # if today is not fri (fri 6pm UTC when reset is)
    # find next fri and say how long it is
    if today_utc.weekday() != 4:
        reset_utc = rel.relativedelta(hour=18, minute=0, second=0, microsecond=0, days=1, weekday=rel.FR)
        reset = today_utc + reset_utc
        countdown(int((reset-today_utc).total_seconds()))
    # today is fri
    else:
        # we're after 6pm in the day just go about it normally
        if datetime.datetime.utcnow().time() >= datetime.time(18, 0, 0, 0):
            reset_utc = rel.relativedelta(hour=18, minute=0, second=0, microsecond=0, days=1, weekday=rel.FR)
            reset = today_utc + reset_utc
            countdown(int((reset-today_utc).total_seconds()))
        # otherwise don't go to any other day, just give the 18hr countdown
        else:
            reset = today_utc + rel.relativedelta(hour=18, minute=0, second=0, microsecond=0)
            countdown(int((reset-today_utc).total_seconds()))


# finds military time only!
def my_raid():
    running.set(True)

    try:
        int(hour.get())
        int(minute.get())
        int(second.get())
    except ValueError:
        messagebox.showerror("Bad Input", "Please input numbers into the boxes")
        return
    now = datetime.datetime.today()
    try:
        target_time = rel.relativedelta(hour=int(hour.get()), minute=int(minute.get()),
                                        second=int(second.get()), microsecond=0)
        my_time = now + target_time
        if int((my_time-now).total_seconds()) <= 0:
            messagebox.showerror("Bad Input", "Please use military time\nFor PM, simply add 12 hour.")
        countdown(int((my_time-now).total_seconds()))
    except ValueError:
        messagebox.showerror("Bad Input", "Please use:\nBetween 0 and 23 on hours\nBetween 0 and 60 on "
                                          "minutes and seconds.")


def accurate_time():
    global temp
    while temp > -1:
        time.sleep(1)
        temp -= 1


def countdown(work_time):
    global temp
    t1 = threading.Thread(target=lambda: accurate_time())

    try:
        temp = work_time
        t1.start()
    except ValueError:
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

        # we should auto-join here because acc_time can't run, so it joins default below
        if not running.get():
            temp = -1
        else:
            try:
                if thirty_min.get() and temp == 1800:
                    winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
                elif five_min.get() and temp == 300:
                    winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC)
                root.update()
                root.after(1000)
            except _tkinter.TclError:
                temp = -1
                t1.join()
                return
    # setting helps fix stuck 1 left issue as well as go back to default if not running
    hour.set("0")
    minute.set("0")
    second.set("0")
    root.update()
    t1.join()


# nastier than before, but safer to delete the thread
def close_program():
    response = messagebox.askyesno("Reset Countdown - Close?", "Do you want to close the program?")
    if response:
        global temp
        temp = -1
        root.quit()


btn = Button(root, text=" NA ", bd='5', command=na_time)
btn.place(x=20, y=60)
btn = Button(root, text=" EU ", bd='5', command=eu_time)
btn.place(x=65, y=60)
btn = Button(root, text=" Custom Today ", bd='5', command=my_raid)
btn.place(x=20, y=95)

# menu bar
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Reset", command=lambda: running.set(False))
file_menu.add_separator()
file_menu.add_checkbutton(label="5 Minute Reminder Ping", command=lambda: five_min.set(not five_min.get()))
file_menu.add_checkbutton(label="30 Minute Reminder Ping", command=lambda: thirty_min.set(not thirty_min.get()))
file_menu.add_separator()
file_menu.add_command(label="Close", command=close_program)
menu_bar.add_cascade(label="File", menu=file_menu)

# help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Ping Test", command=lambda: winsound.PlaySound("SystemExclamation", winsound.SND_ASYNC))
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)
root.protocol("WM_DELETE_WINDOW", close_program)
root.mainloop()
