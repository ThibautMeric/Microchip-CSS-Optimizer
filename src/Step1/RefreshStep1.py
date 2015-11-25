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
import platform
import os
from Step1.EnableAddCSS import *
from Step1.OpenCSS import *
from Step1.EnableAddHTML import *
from Step1.OpenHTML import *
from Read.ReadFile import*


def RefreshStep1(lfStep1,WindowSetting, HtmlPath, CssPath):
    
    #variable declaration
    NB_CSS=len(CssPath)
    NB_HTML=len(HtmlPath)
    
    #Clean the frame

    for widget in lfStep1.winfo_children():
        widget.grid_forget()

    # Refresh the display
    
    line =0

    lfStep1.children["titlecss"].grid(row=0, column=0, pady="5")
    line+=1
    for i in range(0,NB_CSS):
        NewLabel = Label(lfStep1, text="..." + CssPath[i][int(-40*WindowSetting["Reduce"]):])
        NewLabel.grid(row=line, column=0)
        line+=1
    lfStep1.children["entrycss"].delete(0, END)
    lfStep1.children["entrycss"].insert(0,"Insert Path")
    lfStep1.children["entrycss"].grid(row=line, column=0, pady="5")
    lfStep1.children["browsecss"].grid(row=line, column=1, pady="5")
    line+=1
    lfStep1.children["addcss"].grid(row=line, column=0, pady="5")
    line+=1


    lfStep1.children["titlehtml"].grid(row=line, column=0, pady="5")
    line+=1
    for i in range(0,NB_HTML):
        NewLabel = Label(lfStep1, text="..." + HtmlPath[i][int(-40*WindowSetting["Reduce"]):])
        NewLabel.grid(row=line, column=0)
        line+=1
    lfStep1.children["entryhtml"].delete(0, END)
    lfStep1.children["entryhtml"].insert(0,"Insert Path")
    lfStep1.children["entryhtml"].grid(row=line, column=0, pady="5")
    lfStep1.children["browsehtml"].grid(row=line, column=1, pady="5")
    line+=1
    lfStep1.children["addhtml"].grid(row=line, column=0, pady="5")

    lfStep1.grid(row=1, column=1, sticky="n s e w")
pass

def AddCSS(lfStep1,WindowSetting, HtmlPath, CssPath):
    CssPath.append(lfStep1.children["entrycss"].get())
    RefreshStep1(lfStep1,WindowSetting, HtmlPath, CssPath)
    lfStep1.children["addcss"].configure(state="disabled")
    if(len(HtmlPath)>0):
        lfStep1.children["read"].grid(row=len(CssPath) + len(HtmlPath) + 9, column=0, pady="5")
pass

def AddHTML(lfStep1,WindowSetting, HtmlPath, CssPath):
    HtmlPath.append(lfStep1.children["entryhtml"].get())
    RefreshStep1(lfStep1,WindowSetting, HtmlPath, CssPath)
    lfStep1.children["addhtml"].configure(state="disabled")
    lfStep1.children["read"].grid(row=len(CssPath) + len(HtmlPath) + 9, column=0, pady="5")
pass
