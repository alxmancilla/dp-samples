# A A Model-View-Controller framework for TKinter.
# Model: Data Structure. Controller can send messages to it, and model can respond to message.
# View : User interface elements. Controller can send messages to it. View can call methods from Controller when an event happens.
# Controller: Ties View and Model together. turns UI responses into changes in data and vice versa.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

 
#
#Controller: Ties View and Model together.
#       --Performs actions based on View events.
#       --Sends messages to Model and View and gets responses
#       --Has Delegates
#       --Controllers may talk to other controllers through delegates
 
class MyController():
    def __init__(self,parent):
        self.parent = parent
        self.model = MyModel(self)    # initializes the model
        self.view = MyView(self)  #initializes the view
 
        #initialize properties in view, if any
        pass
 
        #initalize properties in model, if any
        pass
 
#event handlers -- add functions called by command attribute in view
    def someHandelerMethod(self):
        pass
#delegates -- add functions called by delegtes in model or view
    def modelDidChangeDelegate(self):
        pass
 
#View : User interface elements.
#       --Controller can send messages to it.
#       --View can call methods from Controller vc when an event happens.
#       --NEVER communicates with Model.
#       --Has setters and getters to communicate with controller
 
class MyView(Frame):
    def loadView(self):
        pass
    def __init__(self,vc):
        #make the view
        self.frame=Frame()
        self.frame.grid(row = 0,column=0)
 
        #set the delegate/callback pointer
        self.vc = vc
 
        #control variables go here. Make getters and setters for them below
        someControlVariable= StringVar()
        someControlVariable = ('nil')
 
        #load the widgets
        self.loadView()
    #Getters and setters for the control variables.
    def getSomeControlVariable(self):
    #returns a string of the entry text
        return self.entry_text.get()
    def setSomeControlVariable(self,text):
    #sets the entry text given a string
        self.entry_text.set(text)
 
#Model: Data Structure.
#   --Controller can send messages to it, and model can respond to message.
#   --Uses delegates from vc to send messages to the Controller of internal change
#   --NEVER communicates with View
#   --Has setters and getters to communicate with Controller
 
class MyModel():
    def __init__(self,vc):
        #set delegate/callback pointer
        self.vc = vc
        #initialize model
        self.myModel = 0
 
#Delegate goes here. Model would call this on internal change
    def modelDidChange(self):
        self.vc.listChangedDelegate()
#Setters and getters for the model
    def getModel(self):
        return self.myModel
    def setList(self,newData):
        self.MyModel = newData
        self.modelDidChange #delegate called on change
#Any internal processing for the model        
 
def main():
    root = Tk()
    frame = Frame(root )
    root.title('MVC Skeleton')
    app = MyController(root)
    root.mainloop()  
 
if __name__ == '__main__':
    main()
