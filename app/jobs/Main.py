#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Main -- shortdesc

Main is a description wurst

It defines classes_and_methods

@author:     Effi

@copyright:  2017 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''
from LED import LED
from Socket import Socket
from datetime import datetime, time
from Controller import Controller
from Belueftung import Belueftung
from Heater import Heater
from SensorTemp import SensorTemp

lichtData = {
     time(07,00) : time(19,00)
    }

#Create objects
temp = SensorTemp(274151, '3AU6RMVSYJ0UXQHY','VBO2U7I3LHBZNX05' )
led = LED("LED Saga", lichtData)
belueftung = Belueftung("Luefter", '23:59:59', '00:00:20')
heater = Heater("Handy Heater", belueftung, temp)
belueftung.setHeater(heater)
controller = Controller(led, belueftung, heater, temp)
controller.BELUEFTUNG.turnOff()
controller.HEATER.turnOff()
controller.LED.turnOff()
controller.start()


