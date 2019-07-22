# RobotNight-VpnLogger
This Robot was written in Python

# Get Started
- If you want to just use it, use the release section to download the latest version
- If you want to contribute with the project... **git clone** and go ahead!

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
1) Running with Python command line (it needs Python installed in your machine)
2) Running the standalone version. Just double click on the **robotnight-vpnlogger.exe**
