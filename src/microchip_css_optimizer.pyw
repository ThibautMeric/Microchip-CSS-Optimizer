# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# coding: utf8

__author__ = "Thibaut MERIC"
__date__ = "$29 oct. 2015 10:35:15$"

#Import

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
from Step1.InitializeStep1 import *
from Step1.RefreshStep1 import *
from Step2.InitializeStep2 import *
from Step3.InitializeStep3 import *
from StepWarning.InitializeWarning import *
import os
import platform
from test import *


        #######################
        ##GENERAL DECLARATION##
        #######################
        
Version = "v0.95"
HtmlPath = []                                                                           # Stores the HTML files path
CssPath = []                                                                            # Stores the CSS files path
Modifier1DataCSS = []                                                                   # Stores the CSS modifier: Element
Modifier2DataCSS = []                                                                   # Stores the CSS modifier: Class
Modifier3DataCSS = []                                                                   # Stores the CSS modifier: ID
Modifier4DataCSS = []                                                                   # Stores the CSS modifier: At-Rule
CssTable = [Modifier1DataCSS, Modifier2DataCSS, Modifier3DataCSS, Modifier4DataCSS]     # Store all the CSS data
ModifierDict = {"Modifier1":"Element", "Modifier2":"Class", "Modifier3":"Id", "Modifier4":"At-Rule"} # Name of Modifiers, default  Element,Class,Id,At-Rule
ButtonList = []                                                                         # List of all the Checkbuttons in the frame selected or not by the user
WarningType1 = []                                                                       # List all the warning type1, Default: No CSS defintion
WarningType2 = []                                                                       # List all the warning type2, Default: Multiple CSS definiton
WarningType3 = []                                                                       # List all the warning type3, Default: CSS not oftenly used
WarningList = [WarningType1, WarningType2, WarningType3]                                  # List of all the Warnings in the warning step
Modifier1DataHTML = []                                                                  # Stores the HTML modifier: Element
Modifier2DataHTML = []                                                                  # Stores the HTML modifier: Class
Modifier3DataHTML = []                                                                  # Stores the HTML modifier: Id
HtmlTable = [Modifier1DataHTML, Modifier2DataHTML, Modifier3DataHTML]                   # Stores Store all the HTML data
CBStep2State = ["", "", "", "", "Select?", ModifierDict["Modifier1"]]                   # Stores the state of the CBSelChoice 0:Modifier1 1:Modifier2 3:Modifier3 4:Modifier4 5:Default 6:Previous Modifier Selected
ChoiceList = ("None", "Default", "Current", "All")
ChoiceList2 = ("View All", "Selected Only", "Not Selected Only")


    ##############################
    ##END OF GENERAL DECLARATION##
    ##############################

Window = Tk()

Window.resizable(width=False, height=False)
Window.title("Microchip CSS Optimizer " + Version)
WindowSetting = {}
if(platform.system() == 'Windows'):
    WindowSetting["Reduce"] = 1
    WindowSetting["Enlarge"] = 1
elif(platform.system() == 'Darwin'):
    WindowSetting["Reduce"] = 0.72
    WindowSetting["Enlarge"] = 1.1
else:
    WindowSetting["Reduce"] = 0.7
    WindowSetting["Enlarge"] = 1.2

        ###############
        ##DEFINITIONS##
        ###############

#Definition for the Global WorkSpace

lfStep1 = tk.LabelFrame(Window, text="Step1:")
lfStep2 = tk.LabelFrame(Window, text="Step2:")
lfWarning = tk.LabelFrame(Window, text="Warning:")
lfStep3 = tk.LabelFrame(Window, text="Step3:")
Bottom = Label(Window, text="2016 - Developped by IoT & HASG Group - " + Version)
Bottom.grid(row=2, column=1)

    ######################
    ##END OF DEFINITIONS##
    ######################
    
InitializeStep1(Bottom, lfStep1, lfStep2, lfWarning, lfStep3, WindowSetting, HtmlPath, CssPath, CssTable, HtmlTable, ModifierDict, WarningList, CBStep2State, ButtonList, ChoiceList, ChoiceList2)
InitializeStep2(lfStep2, ModifierDict, CBStep2State, WindowSetting, ChoiceList, ChoiceList2, Bottom, CssTable,ButtonList)
InitializeWarning(lfWarning, WindowSetting, WarningList)
InitializeStep3(Bottom, lfStep1, lfStep2, lfWarning, lfStep3, WindowSetting, Version, CssTable, HtmlPath, CssPath, HtmlTable, WarningList, CBStep2State, ModifierDict, ChoiceList2)

RefreshStep1(lfStep1, WindowSetting, HtmlPath, CssPath)

Window.mainloop()
