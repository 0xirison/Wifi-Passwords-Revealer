#!/usr/bin/python3
import subprocess
import datetime
import os
import platform

if "windows" in platform.system().lower():
    try:
        print(
            """
 ________ __   ___ __
|  |  |  |__|.'  _|__|
|  |  |  |  ||   _|  |
|________|__||__| |__|

 ______                                           __
|   __ \.---.-.-----.-----.--.--.--.-----.----.--|  |.-----.
|    __/|  _  |__ --|__ --|  |  |  |  _  |   _|  _  ||__ --|
|___|   |___._|_____|_____|________|_____|__| |_____||_____|

 ______                           __
|   __ \.-----.--.--.-----.---.-.|  |.-----.----.
|      <|  -__|  |  |  -__|  _  ||  ||  -__|   _|
|___|__||_____|\___/|_____|___._||__||_____|__|

==========================
Wifi Passwords Revealer v1.0
Author: irison
GitHub: https://github.com/0xirison
*._.* __ _ ._
|[  |_) (_)[ )
==========================
""")

        wifi_list = []
        wifi_dict = {}
        show_wifi_command = subprocess.run(
            "netsh wlan show profile ", shell=False, stdout=subprocess.PIPE
        )

        for line in show_wifi_command.stdout.decode("latin-1").splitlines():
            if "All" in line.replace(" ", ""):
                delim = ": "
                ssid = line[line.index(delim) + len(delim):]
                if " " in ssid:
                    ssid = '"{}"'.format(ssid)
                    wifi_list.append(ssid)
                else:
                    wifi_list.append(ssid)
        for wifi_details in wifi_list:
            show_wifi_password = subprocess.run(
                "netsh wlan show profile " + "name=" + wifi_details + " key=clear",
                shell=False,
                stdout=subprocess.PIPE,
            )
            for line in show_wifi_password.stdout.decode("latin-1").splitlines():
                if "Key Content" in line.replace("\r\n", "").strip():
                    delim = ": "
                    wifi_dict[wifi_details] = line[line.index(
                        delim) + len(delim):]
                else:
                    continue
        file = open(
            os.path.normpath(os.path.expanduser(
                "~/Desktop")).replace("\\", "\\\\")
            + "\\Wifi_Passwords-"
            + str(datetime.datetime.now())
            .replace(":", "-")
            .replace(" ", "-")
            .split(".")[0]
            + ".txt",
            "w",
        )
        for key, values in wifi_dict.items():
            file.write(key + ": " + values + "\r\n")
        file.close()
        print(
            "[+] All your previous logged-in Wifi SSIDs and passwords are saved on your Desktop!"
        )
    except:
        print(
            "[-] Sorry, this windows system version does not support the used utility commands"
        )

else:
    print("[-] Sorry, this tool works only on Windows systems")
