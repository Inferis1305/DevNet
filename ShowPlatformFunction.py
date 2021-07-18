from netmiko import ConnectHandler
import datetime
import os
import os.path
from os import path
import re
import pyinputplus as pyip

def GenShowPatform(SiteCode,PSTN_GW_DB):
    #
    py_file_location=os.path.dirname(os.path.abspath(__file__))
    os.chdir(py_file_location+"\\"+SiteCode)
    #
    net_connect = ConnectHandler(
        device_type = "cisco_ios",
        host = PSTN_GW_DB[0],
        username = "cisco",
        password = "cisco",
        secret = "cisco" 
    )
    command = "show platform"
    print(net_connect.find_prompt())
    output = net_connect.send_command(command)
    #print(output)
    ConfigFile= open(str(SiteCode) + "_show_platform.txt","w+")
    ConfigFile.write(output)
    ConfigFile.close()
    net_connect.disconnect()
    return output