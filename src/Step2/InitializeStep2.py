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
from Step2.RefreshStep2 import*
import platform

def InitializeStep2(lfStep2, ModifierDict, CBStep2State, WindowSetting, ChoiceList, ChoiceList2, Bottom, CssTable,ButtonList):

    #Definition for Step 2

        #            Parent             ----------------------->                 Children
        #Managed by : grid   |   grid   |      pack        |  pack |  none |    grid    |
        #           |  Id:1  |   Id:2   |      Id:3        |  Id:4 |  Id:5 |      Id:6  |
                    #lfStep2->lfModifier->ModifierWorkspace->canvas->frame->Checkbuttons
                    #   \\\\\\TitleStep2                  \scrollbar
                    #    \\\\\CBModifier
                    #     \\\\CBSelChoice
                    #      \\\CBViewChoice
                    #       \\SearchBar
                    #        \BSearch

    #############################Id:2 definition########################################

    lfModifier = tk.LabelFrame(lfStep2, name="lfmodifier")
    TitleStep2 = Label(lfStep2, text="Select the desired definition to add to your CSS", name="titlestep2")
    ModifierList = (ModifierDict["Modifier1"], ModifierDict["Modifier2"], ModifierDict["Modifier3"], ModifierDict["Modifier4"])
    CallRefreshStep2 = lambda event: RefreshStep2("", Bottom, lfStep2, CBStep2State, ModifierDict, CssTable, ButtonList, ChoiceList, ChoiceList2, WindowSetting)
    CBModifier = ttk.Combobox(lfStep2, values=ModifierList, state='readonly', name="cbmodifier")
    CBModifier.set(ModifierList[0])
    CBModifier.bind('<<ComboboxSelected>>', CallRefreshStep2)
    CBSelChoice = ttk.Combobox(lfStep2, values=ChoiceList, state='readonly', name="cbselchoice")
    CBSelChoice.set(CBStep2State[4])
    CBSelChoice.bind('<<ComboboxSelected>>',CallRefreshStep2)
    CBViewChoice = ttk.Combobox(lfStep2, values=ChoiceList2, state='readonly', name="cbviewchoice")
    CBViewChoice.set(ChoiceList2[0])
    CBViewChoice.bind('<<ComboboxSelected>>', CallRefreshStep2)
    SearchBar = Entry(lfStep2, width=int(20*WindowSetting["Reduce"]), name="searchbar")
    CallRefreshStep2ForButton = lambda: RefreshStep2("", Bottom, lfStep2, CBStep2State, ModifierDict, CssTable, ButtonList, ChoiceList, ChoiceList2, WindowSetting)
    if(platform.system() == 'Windows'):BSearch = ttk.Button(lfStep2, text="Search", command=CallRefreshStep2ForButton, name="bsearch")
    else: BSearch = tk.Button(lfStep2, text="Search", command=CallRefreshStep2ForButton, name="bsearch")
    SearchBar.bind("<Return>",CallRefreshStep2)
    #############################Id:3 definition########################################

    ModifierWorkspace = tk.Frame(lfModifier, name="modifierworkspace")
    ModifierWorkspace.grid(row=1, column=2, sticky="n s e w")
    #############################Id:4 definition########################################

    canvas = Canvas(ModifierWorkspace, name="canvas")
    myscrollbar = Scrollbar(ModifierWorkspace, orient="vertical", command=canvas.yview, name="myscrollbar")
    canvas.configure(yscrollcommand=myscrollbar.set)
    #############################Id:5 definition########################################

    frame = Frame(canvas, name="frame")
    canvas.create_window((0, 0), window=frame, anchor='nw')
pass