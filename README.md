# Auto Hathway Login 

This is a small script that will log you in automatically if Hathway logs you out. Hathway kicks you out every few hours and this is very annoying while downloading huge files. This script requires Python 2.7

Usage:

```
python AutoHathwayLogin.py <username> <password> <sleep time in seconds>

```

Where username is your hathway email, password is your password and sleep time is the time between 2 consecutive internet connectivity tests and default is 30seconds. You can alternatively save username and password in the variables in the file and simply run by typing

```
python AutoHathwayLogin.py
```