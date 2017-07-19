'''
Created on 11.05.2017

@author: Effi
'''
from Socket import Socket
from datetime import datetime
class LED(Socket):
    '''
    classdocs
    '''
    codeOn = 5510417
    codeOff = 5510420
    state = "OFF"

    def __init__(self, name, laufzeit):
        '''
        Constructor
        '''
        self.name = name
        self.laufzeit = laufzeit 
    def checkTime(self):
        now = datetime.now()
        now_time = now.time()
        tmp = False
        for key in self.laufzeit:
            start = key
            end = self.laufzeit[key]
            
            if now_time >= start  and now_time <= end:
                return True
            else:
                tmp = False
        
        return tmp
    def turnOn(self):
        self.state = "ON"
        Socket.turnOn(self, self.codeOn, 'Licht an!') 
    def turnOff(self):
        self.state = "OFF" 
        return Socket.turnOff(self, self.codeOff, 'Licht aus!')
    def update(self):
        #print datetime.time(datetime.now())
        #print datetime
        if self.state == "OFF" and self.checkTime():
            self.turnOn()
        elif self.state == "ON" and not(self.checkTime()):
            self.turnOff()
        else:
            return False