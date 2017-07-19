'''
Created on 11.05.2017

@author: Effi
'''
import os
from datetime import datetime
from datetime import timedelta
class Socket(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def turnOn(self, codeOn, text):
        print text
        for i in range(10):
            os.system("sudo /home/pi/myProject/433Utils/RPi_utils/codesend " + str(codeOn))
        return True
    def turnOff(self, codeOff, text):
        print text
        for i in range(10):
            os.system("sudo /home/pi/myProject/433Utils/RPi_utils/codesend " + str(codeOff))
        return True
    def addtoTime(self, currentAsString, period):
        timeList = [currentAsString, period]
        totalSecs = 0
        for tm in timeList:
            timeParts = [int(s) for s in tm.split(':')]
            totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
        totalSecs, sec = divmod(totalSecs, 60)
        hr, min = divmod(totalSecs, 60)
        if hr >= 24:
            return datetime.strptime("00:00:00", '%H:%M:%S')
        datetime.now()
        return datetime.strptime("%d:%02d:%02d" % (hr, min, sec), '%H:%M:%S')
    
    def getTimeList(self, period, sleep):
        tmp = {}
        current = datetime.strptime("00:00:00", '%H:%M:%S')
        currentAsString = current.strftime("%H:%M:%S")

        while True:
            
            plusOne = self.addtoTime(currentAsString, period)           
            
            tmp[current] = plusOne
            
            current = plusOne
            currentAsString = current.strftime("%H:%M:%S")
            
            plusOne = self.addtoTime(currentAsString, sleep)
            
            current = plusOne
            currentAsString = current.strftime("%H:%M:%S")
                        
            if  current == datetime.strptime("00:00:00", '%H:%M:%S'):
                break

        return tmp 
