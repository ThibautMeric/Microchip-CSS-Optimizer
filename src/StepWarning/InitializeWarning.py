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
from StepWarning.RefreshWarning import*
import platform

def InitializeWarning(lfWarning, WindowSetting, WarningList):

    #Definition for Warning

        #            Parent             ----------------------->                       Children
        #Managed by :  grid    | pack |         grid            |   pack/grid  |  none | grid  |
        #           |  Id:1    | Id:2 |         Id:3            |     Id:4     |  Id:5 | Id:6  |
                    #lfWarning->frame4->ModifierWorkspaceWarning->CanvasWarning->frame2->Labels
                    #                 \                           \myscrollbar2
                    #                  \______TopBarPack--------->TitleTBP
                    #                                           \\EntrySelector
                    #                                            \RefreshButton


    #############################Id:2 definition########################################

    frame4 = Frame(lfWarning, name="frame4")

    #############################Id:3 definition########################################

    ModifierWorkspaceWarning = tk.LabelFrame(frame4, name="modifierworkspacewarning")
    ModifierWorkspaceWarning.grid(row=1, column=2, sticky="n s e w")
    TopBarPack = Frame(frame4)

    #############################Id:4 definition########################################

    CanvasWarning = Canvas(ModifierWorkspaceWarning, name="canvaswarning")
    myscrollbar2 = Scrollbar(ModifierWorkspaceWarning, orient="vertical", command=CanvasWarning.yview, name="myscrollbar2")
    CanvasWarning.configure(yscrollcommand=myscrollbar2.set)

    TopBarPack = Frame(frame4, name="topbarpack")
    TitleTBP = tk.Label(TopBarPack, text="Hide Warnings: Name or PartName* are valid. Space required between elements", name="titletbp")
    TextSelector = StringVar()
    TextSelector.set("!DOCTYPE head meta div script title html body")
    EntrySelector = Entry(TopBarPack, textvariable=TextSelector, width=int(100*WindowSetting["Reduce"]), name="entryselector")
    CallRefreshWarning = lambda: RefreshWarning(lfWarning, WarningList, WindowSetting)
    CallRefreshWarningForEntry = lambda event: RefreshWarning(lfWarning, WarningList, WindowSetting)
    EntrySelector.bind("<Return>",CallRefreshWarningForEntry)
    if(platform.system() == 'Windows'):RefreshButton = ttk.Button(TopBarPack, text="Refresh", command=CallRefreshWarning, name="refreshbutton")
    else:RefreshButton = tk.Button(TopBarPack, text="Refresh", command=CallRefreshWarning, name="refreshbutton")
    #############################Id:5 definition########################################

    frame2 = Frame(CanvasWarning, name="frame2")
    CanvasWarning.create_window((0, 0), window=frame2, anchor='nw')
    CanvasWarning.configure(width=1000, height=200)
pass
