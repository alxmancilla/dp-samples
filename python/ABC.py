#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
 
class AbstractAnimal(metaclass=ABCMeta):
     
    @abstractmethod
    def makeSound(self):
        pass

    @abstractmethod
    def getName(self):
        pass        

class Dog(AbstractAnimal):
    def __init__(self):
        self.name="dog"
        print("instantianting a derived class")
        
    def makeSound(self):
        return "guau-guau!"
    
    def getName(self):
        return self.name
        
if __name__ == "__main__":
    animal = Dog()
    print("animal: {:s}, hace sonido {:s}".format(animal.getName(),animal.makeSound()))
 