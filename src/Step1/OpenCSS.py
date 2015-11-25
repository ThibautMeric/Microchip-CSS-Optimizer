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
        
def OpenCSS(lfStep1):
    filepath1 = askopenfilename(title="Open a file", filetypes=[('CSS files', '.css')])
    if len(filepath1)>0:
        lfStep1.children["entrycss"].delete(0, END)
        lfStep1.children["entrycss"].insert(0,filepath1)
        lfStep1.children["entrycss"].xview_moveto(1)
        lfStep1.children["addcss"].configure(state="active")
pass