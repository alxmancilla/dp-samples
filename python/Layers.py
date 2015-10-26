#!/usr/bin/env python
# -*- coding: utf-8 -*-

class L1Provider: 
    """ Clase base proveedor nivel 1"""
    def __init__(self):
        self.name = "L1Provider" 
    def l1Service(self):
        pass
    
class L2Provider:
    """ Clase base proveedor nivel 2"""
    def __init__(self):
        self.name = "L2Provider"
    def l2Service(self):
        pass
    def setLowerLayer(self, lowerLayer):
        self.lowerLayer = lowerLayer
        
class L3Provider:
    """ Clase base proveedor nivel 3"""
    def __init__(self):
        self.name = "L3Provider"
    def l3Service(self):
        pass
    def setLowerLayer(self, lowerLayer):
        self.lowerLayer = lowerLayer

class DataLayer(L1Provider):
    def l1Service(self):
        print("Executing %s Service" % self.name);
        
class LogicLayer(L2Provider):
    def l2Service(self):
        print("Starting %s Service" % self.name)
        self.lowerLayer.l1Service()
        print("Finishing %s Service" % self.name)
        
class PresentationLayer(L3Provider):
    def l3Service(self):
        print("Starting %s Service" % self.name)
        self.lowerLayer.l2Service()
        print("Finishing %s Service" % self.name)
        
# Execute if this file is run as a script and not imported as a module
if __name__ == "__main__":
    ui = PresentationLayer()
    business = LogicLayer()
    data = DataLayer()
    
    ui.setLowerLayer(business)
    business.setLowerLayer(data)
    
    ui.l3Service();
