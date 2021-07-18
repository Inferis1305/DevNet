import datetime
import os
import os.path
from os import path
import re
import pyinputplus as pyip
#
#SiteCode = pyip.inputStr(prompt='Enter a Site Code: ')
#if len(SiteCode) > 5:
#    print("Not a valid site code. Max 5 charters are allowed. You have in your input",len(SiteCode) )
#    exit()
# DataBase 
CMGroup1_2 = ['Aichach','Altötting','Alzenau','Amberg','Ansbach','Aschaffenburg','Augsburg','Schwabmünchen','Donauwörth','Bad Kissingen','Bad Neustadt','Mellrichstadt','Bad Reichenhall','Bamberg']
CMGroup2_1 = ['Bayreuth','Bemau','Cham','Coburg','Dachau','Deggendorf','Dillingen a.d. Donau','Ebersberg','Ebrach','Eggenfelden','Eichstätt','Erding','Erlangen','Forchheim','Freyung','Fürstenfeldbruck','Fürth','Garmisch-Partenkirchen','Gemünden','Günzburg','Haßfurt','Hersbruck','Hof']
CMGroup4_5 = ['Amberg','Hof','Ingolstadt','Kaisheim','Kaufbeuren','Kelheim','Kempten','Kitzingen','Kronach','Kulmbach','Landau a.d. Isar','Landsberg a. Lech','Landshut','Laufen','Lichtenau','Lichtenfels']
CMGroup5_4 = ['München','Neu-Ulm','Neuburg','Neumarkt','Neustadt','Niederschönenfeld','Nördlingen','Nürnberg','Obernburg','Passau']
CMGroup3_6 = ['Freising','Garmisch-Partenkirchen','Gemünden','Lindau','Memmingen','Illertissen','Neu Ulm','Memmingen','Miesbach','Miltenberg','Mühldorf a. Inn','Passau','Pegnitz','Pfaffenhofen','Rain am Lech','Regensburg','Rosenheim','Rothenfeld','Schwabach','Schwandorf','Schweinfurt','Sonthofen','Starnberg','Straubing']
CMGroup6_3 = ['Tirschenreuth','Traunstein','Viechtach','Weiden','Weilheim','Weissenburg i.Bay','Wolfratshausen','Wunsiedel','Würzburg']

CMGroup1_2net = ['CMGroup1_2','Sub1','Sub2','Nxx03ZSH014vw','Mxx13ZSH006vw','10.216.3.14','10.216.1.6']
CMGroup2_1net = ['CMGroup2_1','Sub2','Sub1','Mxx13ZSH006vw','Nxx03ZSH014vw','10.216.1.6','10.216.3.14']
CMGroup4_5net = ['CMGroup4_5','Sub4','Sub5','Nxx03ZSH015vw','Mxx13ZSH007vw','10.216.3.15','10.216.1.7']
CMGroup5_4net = ['CMGroup5_4','Sub5','Sub4','Mxx13ZSH007vw','Nxx03ZSH015vw','10.216.1.7','10.216.3.15']
CMGroup3_6net = ['CMGroup3_6','Sub3','Sub6','Nxx03ZSH010vw','Mxx13ZSH010vw','10.216.3.10','10.216.1.10']
CMGroup6_3net = ['CMGroup6_3','Sub6','Sub3','Mxx13ZSH010vw','Nxx03ZSH010vw','10.216.1.10','10.216.3.10'] 

def FindCUCM_Group(SearchCUCM_Group):
    print("Searching for name:",SearchCUCM_Group)
    if SearchCUCM_Group in CMGroup1_2:
        #print("Found",SearchCUCM_Group,"in group CMGroup1_2")
        return CMGroup1_2net
    elif SearchCUCM_Group in CMGroup2_1:
        #print("Found",SearchCUCM_Group,"in group CMGroup2_1")
        return CMGroup2_1net
    elif SearchCUCM_Group in CMGroup4_5:
        #print("Found",SearchCUCM_Group,"in group CMGroup4_5")
        return CMGroup4_5net
    elif SearchCUCM_Group in CMGroup5_4:
        #print("Found",SearchCUCM_Group,"in group CMGroup5_4")
        return CMGroup5_4net
    elif SearchCUCM_Group in CMGroup3_6:
        #print("Found",SearchCUCM_Group,"in group CMGroup3_6")
        return CMGroup3_6net
    elif SearchCUCM_Group in CMGroup6_3:
        #print("Found",SearchCUCM_Group,"in group CMGroup6_3")
        return CMGroup6_3net
    else:
        return"NotFound"

#SearchCUCM = FindCUCM_Group("Neustadt")
#print(SearchCUCM)
