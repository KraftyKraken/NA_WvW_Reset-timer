# What <h8> 
WvW Reset Countdown is a tool for Guild Wars 2, for simply clicking a button and having the time before WvW NA/EU reset become displayed for you along with the option of a custom time today.

# Limitations <h8> 
Only one countdown timer at the moment is shown and working at a time.
The current build should only work on windows 10. Sorry about that, and I don't have other environments to test it at this time or virtual environments correctly setup to do so.

# Installation <h8> 
To "install", grab the zip file and take the folder out and use the .exe inside the folder. The .exe has to be with its buddy, the icon file, but otherwise you can run the .exe inside the folder from anywhere. \
Desktop? No problem.\
C:\WvW Reset Countdown v2.X? Go for it. \
E:\Look\at\this\terrible\file\structure\WvW Reset Countdown v2.X? You bettcha. It should be very stand alone.\
You can also create a shortcut to the .exe to run it without having to open the folder.

# Known Bugs <h8> 
Please let your local kraken know of any bugs/incompatabilities.\
Known:\
-Doesn't play well with MAC or Linux. Not much I can do here yet besides tell you how to make it.\
-Windows think it's evil because of a lack of cert. It's not, you can look here and see the evilest thing are those global variables.\
-Can't find icon. Not really a bug. But please place it back with it's "icon.ico" friend.\
-Slow visual updates. This isn't something I'm in control of; that's tkinter.\
-Timing is not 100% exact. Because of time to draw the item and check, the miliseconds aren't 100% the same. It's still within the same second.


# How to Build <h8> 
Required to build from .py file are: \
python 3.8+\
dateutil (pip install python-dateutil)\
and pyinstaller (pip install pyinstaller). \
You'll also need to supply a version-info file if you want versioning on it, but 100% requires an icon named "icon.ico" now. Find a neat one. 

# Buy this kraken a cookie? <h8>
Like what I've made? Please consider buying me a cookie for a job well done. Not a coffee. Sorry, I'm just not a fan. Tea's fine though.\
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate?business=G7EXP3LP9UGLW&item_name=Buy+kraken+a+cookie?&currency_code=USD)
