# RobotNight-VpnLogger <img src="https://github.com/ericserafim/RobotNight-VpnLogger/blob/master/app-icon.svg" width="200px" align="right">
You need just one click to log in your VPN. Robot Night will open RSA to get a token and then login GlobalProtect. It is easy as like as you are reading!

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/release-latest-blue.svg)](https://github.com/ericserafim/RobotNight-VpnLogger/releases/latest)

### Dependencies
[![Python 3.7.3](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Generic badge](https://img.shields.io/badge/pywinauto-latest-blue.svg)](https://pywinauto.readthedocs.io/en/latest/)
[![Generic badge](https://img.shields.io/badge/pyperclip-latest-blue.svg)](https://pypi.org/project/pyperclip/)
[![Generic badge](https://img.shields.io/badge/pyautogui-latest-blue.svg)](https://pyautogui.readthedocs.io/en/latest/)

# Get Started
- If you want to just use it, use the [![Generic badge](https://img.shields.io/badge/release-latest-blue.svg)](https://github.com/ericserafim/RobotNight-VpnLogger/releases/latest) to download the latest version
- If you want to contribute with the project... **git clone** and go ahead!<br/>
## ******** It works only with GlobalProtect VPN ********

# How Do I use it?
At first, you should configure Robot Night properly. To do that you need to create the **appsettings.json** file following the instructions below:
1) Open the **appsettings-example.json**
2) Change the data as your environment needs
3) Path tags: They are usually in these locations, but you can change if you need.
4) After your changes, save this file as **appsettings.json** in the project folder

### appsettings example content
```
{
    "rsa" : {
        "pin" : "<your pin>",        
        "path" : "C:\\Program Files\\RSA SecurID Software Token\\SecurID.exe"
    },
    "global_protect" : {
        "username" : "<your username>",
        "password" : "<your password>",
        "path" : "C:\\Program Files\\Palo Alto Networks\\GlobalProtect\\PanGPA.exe"
    },
    "setup" : {
        "timeout" : 30,
        "assets_dir" : "./assets/"
    }
}
```

### Running Robot Night
To run the project you can use two different approaches:
1) Running with Python command line **"python vpnLogger.py"** or using **executor.bat** (it needs Python installed in your machine).
2) Running the standalone version. Just double click on the **RobotNight-VpnLogger.exe**

# How Do I create my own EXE file?
To create your own exe file you should install [![Generic badge](https://img.shields.io/badge/pyinstaller-latest-blue.svg)](https://www.pyinstaller.org/downloads.html) and follow the steps on <a href="https://pyinstaller.readthedocs.io/en/stable/usage.html">docs page</a> <br/>
Also, you can run the command line **"pyinstaller robotnight.spec"**. The **robotnight.spec** file you can find in the files tree of this project.

