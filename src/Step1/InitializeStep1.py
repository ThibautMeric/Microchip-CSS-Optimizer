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
from Read.ReadFile import *
from Step1.EnableAddCSS import *
from Step1.EnableAddHTML import *
from Step1.OpenCSS import *
from Step1.OpenHTML import *
from Step1.RefreshStep1 import *
import platform

def InitializeStep1(Bottom, lfStep1, lfStep2, lfWarning, lfStep3, WindowSetting, HtmlPath, CssPath, CssTable, HtmlTable, ModifierDict, WarningList, CBStep2State, ButtonList, ChoiceList, ChoiceList2):

    #Definition for Step 1

    TitleCss = tk.Label(lfStep1, text="Add a CSS file", name="titlecss")

    CallAddCSS = lambda: AddCSS(lfStep1, WindowSetting, HtmlPath, CssPath)
    CallAddCSSForEntry = lambda event: AddCSS(lfStep1, WindowSetting, HtmlPath, CssPath)
    if(platform.system() == 'Windows'):AddCss = ttk.Button(lfStep1, text="Add CSS file", command=CallAddCSS, state="disable", width=int(15 * WindowSetting["Reduce"]), name="addcss")
    else:AddCss = tk.Button(lfStep1, text="Add CSS file", command=CallAddCSS, state="disable", width=int(15 * WindowSetting["Reduce"]), name="addcss")

    TextCss = StringVar()
    TextCss.set("Insert Path")
    CallEnableAddCss = lambda event: EnableAddCss(AddCss,entryCss.get())
    entryCss = tk.Entry(lfStep1, textvariable=TextCss, width=int(42 * WindowSetting["Reduce"]), name="entrycss")
    entryCss.bind("<Key>",CallEnableAddCss)
    entryCss.bind("<Return>",CallAddCSSForEntry)

    CallOpenCSS = lambda: OpenCSS(lfStep1)
    if(platform.system() == 'Windows'):BrowseCss = ttk.Button(lfStep1, text="Browse", command=CallOpenCSS, width=int(10 * WindowSetting["Reduce"]), name="browsecss")
    else:BrowseCss = tk.Button(lfStep1, text="Browse", command=CallOpenCSS, width=int(10 * WindowSetting["Reduce"]), name="browsecss")


    TitleHtml = tk.Label(lfStep1, text="Add an HTML file", name="titlehtml")

    CallAddHTML = lambda: AddHTML(lfStep1, WindowSetting, HtmlPath, CssPath)
    CallAddHTMLForEntry = lambda event: AddHTML(lfStep1, WindowSetting, HtmlPath, CssPath)
    if(platform.system() == 'Windows'):AddHtml = ttk.Button(lfStep1, text="Add HTML file", command=CallAddHTML, state="disable", width=int(15 * WindowSetting["Reduce"]), name="addhtml")
    else:AddHtml = tk.Button(lfStep1, text="Add HTML file", command=CallAddHTML, state="disable", width=int(15 * WindowSetting["Reduce"]), name="addhtml")

    TextHtml = StringVar()
    TextHtml.set("Insert Path")
    CallEnableAddHtml = lambda event: EnableAddHtml(AddHtml, entryHtml.get())
    entryHtml = tk.Entry(lfStep1, textvariable=TextHtml, width=int(42 * WindowSetting["Reduce"]), name="entryhtml")
    entryHtml.bind("<Key>",CallEnableAddHtml)
    entryHtml.bind("<Return>",CallAddHTMLForEntry)

    CallOpenHTML = lambda: OpenHTML(lfStep1)
    if(platform.system() == 'Windows'):BrowseHtml = ttk.Button(lfStep1, text="Browse", command=CallOpenHTML, width=int(10 * WindowSetting["Reduce"]), name="browsehtml")
    else:BrowseHtml = tk.Button(lfStep1, text="Browse", command=CallOpenHTML, width=int(10 * WindowSetting["Reduce"]), name="browsehtml")


    CallReadFile = lambda: ReadFile(Bottom, lfStep1, lfStep2, lfWarning, lfStep3, CssPath, HtmlPath, CssTable, HtmlTable, ModifierDict, WarningList, CBStep2State, ButtonList, ChoiceList, ChoiceList2, WindowSetting)
    if(platform.system() == 'Windows'):Read = ttk.Button(lfStep1, text="Read CSS file", command=CallReadFile, width=int(15 * WindowSetting["Reduce"]), name="read")
    else:Read = tk.Button(lfStep1, text="Read CSS file", command=CallReadFile, width=int(15 * WindowSetting["Reduce"]), name="read")
pass
