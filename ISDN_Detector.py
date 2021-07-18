import datetime
import os
import os.path
from os import path
import re
import pyinputplus as pyip
from ShowPlatformFunction import GenShowPatform

#### Detect Platform info file #####
#rootdir = os.getcwd()
#regex = re.compile('(?=.*platform).*(?=.*txt$)')
#
#for root, dirs, files in os.walk(rootdir):
#  for file in files:
#   if regex.match(file):
#        print(file)
#        DCS_file=file
#

def FindISDN(SiteCode,PSTN_GW_DB):
    regex_BRI = re.compile('(?=.*BRI).*(?=.*ok)')
    regex_PRI = re.compile('(?=.*E1).*(?=.*ok)')
    interface_type = "NotFound"
    interface_count = 0
    py_file_location=os.path.dirname(os.path.abspath(__file__))
    os.chdir(py_file_location+"\\"+SiteCode)
    if path.exists(str(SiteCode) + '_show_platform.txt') != True:
        print("Module ISDN Detector: the offline TXT file with show platform is not avallable")
        response = pyip.inputYesNo(prompt="Should I try to connect to device: "+str(PSTN_GW_DB[0])+" ? yes/no: ")
        if response == "no":
            exit()
        if response == "yes":
            RequestShowPaltform = GenShowPatform(SiteCode,PSTN_GW_DB)
    if path.exists(str(SiteCode) + '_show_platform.txt') != True:
        print("Module ISDN Detector: the offline TXT file with show platform is not avallable")
        exit()
    with open(str(SiteCode) + '_show_platform.txt') as fp:
        line = fp.readline()
        cnt = 1
        while line:
            if regex_BRI.findall(line.strip()):
    #           print(line.strip())
                interface_count +=1
                interface_type = "BRI"
            elif regex_PRI.findall(line.strip()):
    #           print(line.strip())
                interface_count +=1
                interface_type = "PRI"
            line = fp.readline()
            cnt += 1
    ISDN = [interface_type,interface_count]
 #   print(ISDN)
    return ISDN

