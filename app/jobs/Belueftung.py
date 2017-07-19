'''
Created on 11.05.2017

@author: Effi
'''
from datetime import datetime
from Socket import Socket

class Belueftung(Socket):
    '''
    classdocs
    '''
    codeOn = 5509457
    codeOff = 5509460
    state = "OFF"

    def __init__(self, name, period, sleep):
        '''
        Constructor
        '''
        self.name = name
        self.laufzeit = self.getTimeList(period, sleep) 
    def checkTime(self):
        currentTime = datetime.time(datetime.now())
        tmp = False
        for key in self.laufzeit:
            x = datetime.time(key) 
            
            if x <= currentTime and datetime.time(self.laufzeit[key]) >= currentTime:
                return True
        
        return tmp
    def turnOn(self):
        self.state = "ON"
        Socket.turnOn(self, self.codeOn, 'Luefter an') 

    def setHeater(self, heater):
        self.heater = heater
        
    def turnOff(self):
        self.state = "OFF" 
        return Socket.turnOff(self, self.codeOff, 'Luefter aus')
    
    def update(self):
        if self.state == "OFF" and self.checkTime() and self.heater.state == "OFF":
            self.turnOn()
            return False
        elif self.state == "ON" and not(self.checkTime()):
            self.turnOff()
            return True
        else:
            return False
