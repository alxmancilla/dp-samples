from tkinter import *
from tkinter import ttk
from tkinter import messagebox
  
  
class MyViewController():
    def __init__(self,parent):
        self.parent = parent;      
          
#(6)added instantiation of view 2014 May 26
        self.view = MyView(self)
 
#Handlers -- target action
    def addPressed(self):
#(7a) Change getters and setters for the view
        self.view.setLabelText(self.view.getType()+ ' is '+ self.view.getAction() + ' Added')
         
    def quitPressed(self):
#(7b) Change getters and setters for the view
        self.view.setLabelText('Quitting')
        answer = messagebox.askokcancel('Ok to Quit','This will quit the program. \n Ok to quit?')
        if answer==True:
            self.parent.destroy()
  
class MyView(Frame):
#(1) Change parent to vc and add a frame 2014 May 26 a  
    def __init__(self,vc):
        self.frame=Frame()
        self.frame.grid(row=0,column=0)
        self.vc = vc
         
        #properties of the view 
        self.labelText = StringVar()
        self.labelText.set("... Ready!!")
        self.Type = StringVar()
        self.Type.set('Type')
        self.Action = StringVar()
        self.Action.set('Action')
#(2)remove self.vc here as vc calls this, not the othere way around.   2014 May 26
#        self.vc = MyViewController(self)
        self.loadView()
#       self.makeStyle()
          
#Handlers -- our pseudo-controller
#(3)removed from application 2014-May-26
#    def addPressed(self):
#        self.labelText.set(self.Type.get()+ '  '+ self.Action.get() + ' Added')
#    def quitPressed(self):
#        self.labelText.set('Quitting')
#        answer = messagebox.askokcancel('Ok to Quit','This will quit the program. \n Ok to quit?')
#        if answer==True:
#            self.parent.destroy()
 
#(4)added setters and getters for the properties 2014-May 26
    def setLabelText(self,newText):
        self.labelText.set(newText)
    def getLabelText(self):
        return self.labelText.get()
    def setType(self,newType):
        self.Type.set(newType)
    def getType(self):
        return self.Type.get()
    def setAction(self,newAction):
        self.Action.set(newAction)
    def getAction(self):
        return self.Action.get()
     
 
#Style Sheet
    def makeStyle(self):
        self.s = ttk.Style()
        self.s.configure('TFrame',background = '#5555ff')
        self.s.configure('TButton',background = 'blue', foreground = '#eeeeff', font = ('Sans','14','bold'), sticky = EW)
        self.s.configure('TLabel',font=('Sans','16','bold'),background = '#5555ff', foreground = '#eeeeff')
        self.s.map('TButton', foreground = [('hover','#5555ff'), ('focus', 'yellow')])
        self.s.map('TButton', background = [('hover', '#eeeeff'),('focus','orange')])
        self.s.configure('TCombobox',background = '#5555ff',foreground ='#3333ff',font = ('Sans',18))
    
#loading the view
    def loadView(self):
        #label
        status_label = ttk.Label(self.frame, textvariable = self.labelText)
        status_label.grid(row=0,column=0,columnspan=4,sticky=EW)
#(5)changed the command= to refer to the view controller 2014-May-26
    # self.addPressed now is self.vc.addPressed
    # self.quitPressed now is self.vc.quitPressed
 
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
 
 
          
def main():
    root = Tk()
#(8) Set up the main loop 2014 May 26
    root.title("My sample MVC")         
    app = MyViewController(root)
    root.mainloop() 
  
  
if __name__ == '__main__':
    main()
    
