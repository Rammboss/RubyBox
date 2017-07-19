'''
Created on 17.05.2017

@author: Effi
'''

import thingspeak
import time
import Adafruit_DHT
class SensorTemp(object):
    '''
    classdocs
    '''
    def __init__(self, channelID, writeKey, readKey):
        '''
        Constructor
        '''
        self.channelID = channelID
        self.writeKey = writeKey
        self.readKey = readKey
        self.sensor = Adafruit_DHT.DHT22
        self.pin = 27
        self.channel = thingspeak.Channel(id=channelID,write_key=writeKey,api_key=readKey)
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        self.lastTemp = temperature
        self.lastHumidity = humidity

        
    def measure(self, channel):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
            
            # write
            response = channel.update({'field1': temperature, 'field2': humidity})
            self.lastTemp = temperature
            self.lastHumidity = humidity
            
            return [temperature, humidity]
        except:
            print("connection failed")
            return [-1,-1]
            
    def update(self):
        return self.measure(self.channel)
    def getLastTemp(self):
        return self.lastTemp
    def getLastHumidity(self):
        return self.lastHumidity