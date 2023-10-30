# Dynamic Menu with lambda
# Import library
from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        
        # Generate Menu 
        menu = Menu(self.master)
        
        
        fileMenu = Menu(menu, tearoff=False, bg='white', activebackground='red', activeforeground='white')
        fileMenu.add_command(label="new",  command=lambda:self.fileMenuFunctions("new", 1))
        fileMenu.add_command(label="open", command=lambda:self.fileMenuFunctions("open", 1))
        # ------------------
        fileMenu.add_separator()
        fileMenu.add_command(label="save",    command=lambda:self.fileMenuFunctions("save", 1))
        fileMenu.add_command(label="save as", command=lambda:self.fileMenuFunctions("save as", 1))
        fileMenu.add_command(label="exit",    command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)
        
        editMenu = Menu(menu, )
        editMenu.add_command(label="copy", command=lambda:self.fileMenuFunctions("copy", 1))
        editMenu.add_command(label="Undo", command=lambda:self.fileMenuFunctions("Undo", 1))
        editMenu.add_command(label="Redo", command=lambda:self.fileMenuFunctions("Redo", 1))
        menu.add_cascade(label="Edit", menu=fileMenu)
        
        menu.add_cascade(label="Help")
        
        self.master.config(menu=menu)

    # Exit program function
    def exitProgram(self):
        print("Closing Window...")
        exit()
        
    # Open file function
    def fileMenuFunctions(self, action, number):
        print(f"action{number}:{action}")
        
        

root = Tk()
# New instance of the window
app = Window(root)

# Starts the process  
root.mainloop()
        
