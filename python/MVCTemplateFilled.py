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
		status_label = ttk.Label(self.frame, textvariable = self.labelText)
		status_label.grid(row=0,column=0,columnspan=4,sticky=EW)
    #buttons
        add_button = ttk.Button(self.frame,command= self.vc.addPressed,text = 'Add')
        add_button.grid(row = 2, column = 0)
        quit_button = ttk.Button(self.frame, command = self.vc.quitPressed, text = 'Quit')
        quit_button.grid(row = 2, column = 3)
    #combobox
        Type_values = ['Adele','Emperor','King','Blackfoot']
        Type_combobox = ttk.Combobox(values = Type_values, textvariable = self.Type)
        Type_combobox.grid(row =1, column = 0)
        Action_values = ['Happy','Sad','Angry','Standing','Swimming']
        Action_combobox = ttk.Combobox(values = Action_values, textvariable = self.Action)
        Action_combobox.grid(row=1, column = 3)
 
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
