
# -*- coding: utf-8 -*-
import os
from aiohttp import web
import logging
from unittest.mock import MagicMock, patch
import asyncio
import random
from cbpi.api import *
from smbus import SMBus
from  . import ABE_ADCPi

logger = logging.getLogger(__name__)

def get_Address():
        bus = SMBus(1) # 1 indicates /dev/i2c-1
        addresses = []
        for address in range(128):
            try:
                bus.read_byte(address)
                addresses.append(address)
            except:
                pass
        return addresses

@parameters([Property.Select("Address", get_Address(), description="The I2C actor address."),Property.Select("Port", options=[0x00,0x01,0x02,0x03], description="Port of the Analog-Input-Modul to which the actor is connected")])
class CustomSensor(CBPiSensor):
    
    def __init__(self, cbpi, id, props):
        super(CustomSensor, self).__init__(cbpi, id, props)
        self.value = 0
        self.adress = int(self.props.get("Adress",104))
        self.port = int(self.props.get("Port",0))
        self.bus = SMBus(1) # 1 indicates /dev/i2c-1
        self.adc = ABE_ADCPi.ADCPi(self.bus,self.adress, 18) 
        

    @action(key="Test", parameters=[])
    async def action1(self, **kwargs):
        print("ACTION!", kwargs)

    async def run(self):
        while self.running is True:
            self.value = self.adc.read_grad(1)
            self.push_update(round(self.value,2))
            await asyncio.sleep(1)
    
    def get_state(self):
        return dict(value=self.value)

    def setup(cbpi):
        cbpi.plugin.register("I2CSensor", CustomSensor)
        pass
