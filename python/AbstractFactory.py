#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
 
class Car(metaclass=ABCMeta):
    def __init(self):
        self._name = None
        self._manufacturer = None
        self._maxSpeed = None
        
    def __str__(self):
        return "name {:s}, manufacturer {:s}".format(self.getName(), self.getMaxSpeed())
    
    def getName(self):
        return self._name
        
    def getMaxSpeed(self):
        return self._maxSpeed
        
       
class SportsCar(Car):   
    def __init__(self):
        self._name="Audi TT"
        self._manufacturer = None
        self._maxSpeed = "240km/h"
        
class VWSportsCar(SportsCar):
    def __init__(self):
        self._manufacturer = "VW"
        
class MBSportsCar(SportsCar):
    def __init__(self):
        self._manufacturer = "MB"
        
class StandardFactory():
    
    @staticmethod
    def get_factory(factory):
        if factory == 'vw':
            return VWFactory()
        elif factory == 'mb':
            return MBFactory()
        raise TypeError('Unknown Factory.')

        
class VWFactory(StandardFactory):
    
    def createCar(self, carType):
        self.car = None
        if carType == "sports":
            self.car = VWSportsCar()
        elif carType == "family":
            self.car = VWFamilyCar()
        else: 
            print("Tipo de auto no disponible.")   
        
        return self.car
    
    def doSomething(self):
        print(self.car)
        
        
if __name__ == "__main__":
        myFactory = StandardFactory.get_factory("vw")
        s = myFactory.createCar("sports")
        print(s)
        
