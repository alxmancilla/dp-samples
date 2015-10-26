#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
 
class Car(metaclass=ABCMeta):
    def __init(self):
        self._name = None
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
        self._maxSpeed = "240km/h"
        
        
class FamilyCar(Car):

    def __init__(self):
        self._name="VW Jetta"
        self._maxSpeed = "180km/h"
        
class MyCarFactory:
    
    def createCar(self, carType):
        self.car = None
        if carType == "sports":
            self.car = SportsCar()
        elif carType == "family":
            self.car = FamilyCar()
        else: 
            print("Tipo de auto no disponible.")   
        
        return self.car
    
    def doSomething(self):
        print(self.car)
        
        
if __name__ == "__main__":
        myFactory = MyCarFactory()
        s = myFactory.createCar("sports")
        f = myFactory.createCar("family")
        print(s)
        print(f)
        
