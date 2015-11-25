try:
    import tkinter as tk
    from tkinter.filedialog import *
    import tkinter.ttk as ttk
    import tkinter.messagebox
except:
    import Tkinter as tk
    from tkFileDialog import *
    import ttk as ttk
    import tkMessageBox
    from Tkinter import *

from Step2.SetCurrent import*

class CheckButtonExtended:
    """
    Class enlarging the definiton of Checkbuttons
    """

    def __init__(self,Parent, Name,NameLenght,Variable):
        self.checkbutton = tk.Checkbutton(Parent, text=Name[:NameLenght], onvalue=True, offvalue=False, variable=Variable,command=SetCurrent)
        self.name= Name
        self.variable= Variable
    pass
pass
    