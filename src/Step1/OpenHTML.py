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
    
def OpenHTML(lfStep1):
    filepath2 = askopenfilename(title="Open a file", filetypes=[('HTML files', '.html')])
    if len(filepath2)>0:
        lfStep1.children["entryhtml"].delete(0, END)
        lfStep1.children["entryhtml"].insert(0,filepath2)
        lfStep1.children["entryhtml"].xview_moveto(1)
        lfStep1.children["addhtml"].configure(state="active")
pass