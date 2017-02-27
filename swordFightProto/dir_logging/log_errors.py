'''
Created on Feb 26, 2017

@author: Robert
'''

from datetime import date, datetime

import sys,os
sys.path.append(os.path.realpath('')+'\\dir_params')

def logError(module, function, description):
    today = date.today()
    today = today.timetuple()
    folder = str(today[0])+str(today[1])+str(today[2])
    directory =  os.path.realpath('')+'\\dir_logging\\errors\\'+folder +'\\'
    if os.path.isdir(directory) == False:
        os.makedirs(directory)
    errorFile = open(directory+str(module)+'-'+str(function)+'.txt', 'a')
    errorFile.write(str(datetime.now())+' ' +description +'\n')
    errorFile.close()
    