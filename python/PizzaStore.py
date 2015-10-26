#!c:/Python34/python.exe -u
# -*- coding: utf-8 -*-

class Pizza:
    def __init__(self):
        pass
        
    def prepare(self):
        pass

    def bake(self):
        print("baking pizza")

    def cut(self):
        print("cutting pizza")

    def box(self):
        print("boxing pizza")
    
    def getName(self):
        return self.name
        
    def __str__(self):
        return self.getName()
        
class CheesePizza(Pizza):
    def __init__(self):
        self.name = "CheesePizza"

    def prepare(self):
        print("preparing %s" % self.getName())

        
class PepperoniPizza(Pizza):
    def __init__(self):
        self.name = "PepperoniPizza"
        
    def prepare(self):
        print("preparing %s" % self.getName())

        

class PizzaStore:

    def __init__(self):
        self.name = "Juventina"
        self.pizzaFactory = SimplePizzaFactory()
        
    def getName(self):
        return self.name
        
    def orderPizza(self, pizzaType):
        pizza = None
        
        pizza = self.pizzaFactory.createPizza(pizzaType)
            
        if pizza != None:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.box()
            
        return pizza
        
class SimplePizzaFactory:
    def __init__(self):
        self.name = "SimplePizzaFactory"
        
    def createPizza(self, pizzaType):
        pizza = None
    
        if pizzaType == "cheese":
            pizza = CheesePizza()
        elif pizzaType == "pepperoni":
            pizza = PepperoniPizza()
        else: 
            print("Tipo de pizza no disponible.")   
        
        return pizza
        
if __name__ == "__main__":
    pizzaStore = PizzaStore()
    tipoPizza = "cheese"
    print("entro a la pizzeria {:s} y ordeno pizza {:s}".format(pizzaStore.getName(),tipoPizza))
    pizza = pizzaStore.orderPizza(tipoPizza)
    print("Me llevo la pizza %s" % pizza.getName())
    
