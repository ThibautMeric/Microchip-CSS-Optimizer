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
from Others.Reset import *
from Step3.IsClassic import *
from Step3.IsDotMin import *
import platform

def InitializeStep3(Bottom, lfStep1, lfStep2, lfWarning, lfStep3, WindowSetting, Version, CssTable, HtmlPath, CssPath, HtmlTable, WarningList, CBStep2State, ModifierDict, ChoiceList2):

    #Definition for Step 3
    
    CallIsClassic = lambda: IsClassic(Version, CssTable)
    if(platform.system() == 'Windows'):Generate = ttk.Button(lfStep3, text="Generate", command=CallIsClassic, width=int(15 * WindowSetting["Reduce"]), name="generate")
    else:tk.Button(lfStep3, text="Generate", command=CallIsClassic, width=int(15 * WindowSetting["Reduce"]), name="generate")
    CallIsDotMin = lambda: IsDotMin(Version, CssTable)
    if(platform.system() == 'Windows'):GenerateDotMin = ttk.Button(lfStep3, text="Generate .min", command=CallIsDotMin, width=int(15 * WindowSetting["Reduce"]), name="generatedotmin")
    else:GenerateDotMin = tk.Button(lfStep3, text="Generate .min", command=CallIsDotMin, width=int(15 * WindowSetting["Reduce"]), name="generatedotmin")
    Callreset = lambda: Reset(Bottom, lfStep1, lfStep2, lfWarning, lfStep3, HtmlPath, CssPath, CssTable, HtmlTable, WarningList, CBStep2State, ModifierDict, ChoiceList2, WindowSetting)
    if(platform.system() == 'Windows'):Rst = ttk.Button(lfStep3, text="Select new files", command=Callreset, width=int(15 * WindowSetting["Reduce"]), name="reset")
    else:Rst = tk.Button(lfStep3, text="Select new files", command=Callreset, width=int(15 * WindowSetting["Reduce"]), name="reset")
pass