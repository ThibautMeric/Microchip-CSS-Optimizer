from Step2.FillCanvasStep2 import*
from Step2.ConfigureCanvasStep2 import*


def RefreshStep2(event, Bottom, lfStep2, CBStep2State, ModifierDict, CssTable, ButtonList, ChoiceList, ChoiceList2, WindowSetting):

    # if change Modifier Group Selection

    if(CBStep2State[5] != lfStep2.children["cbmodifier"].get()):

        #Apply the corresponding selection setting (none/default/current/all) when Modifier group is changed by the user

        if(lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier1"]):# Default: if Element
            if(CBStep2State[0] != ""):lfStep2.children["cbselchoice"].set(CBStep2State[0])
            else:lfStep2.children["cbselchoice"].set(CBStep2State[4])
        elif(lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier2"]):# Default: if Class
            if(CBStep2State[1] != ""):lfStep2.children["cbselchoice"].set(CBStep2State[1])
            else:lfStep2.children["cbselchoice"].set(CBStep2State[4])
        elif(lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier3"]):# Default: if Id
            if(CBStep2State[2] != ""):lfStep2.children["cbselchoice"].set(CBStep2State[2])
            else:lfStep2.children["cbselchoice"].set(CBStep2State[4])
        elif(lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier4"]):# Default: if At-rules
            if(CBStep2State[3] != ""):lfStep2.children["cbselchoice"].set(CBStep2State[3])
            else:lfStep2.children["cbselchoice"].set(CBStep2State[4])

        CBStep2State[5] = lfStep2.children["cbmodifier"].get()

    # if change Selection Mode

    else:
        if((CBStep2State[0] != lfStep2.children["cbmodifier"].get()) and (lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier1"])):CBStep2State[0] = lfStep2.children["cbmodifier"].get()
        elif((CBStep2State[1] != lfStep2.children["cbmodifier"].get()) and (lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier2"])):CBStep2State[1] = lfStep2.children["cbmodifier"].get()
        elif((CBStep2State[2] != lfStep2.children["cbmodifier"].get()) and (lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier3"])):CBStep2State[2] = lfStep2.children["cbmodifier"].get()
        elif((CBStep2State[3] != lfStep2.children["cbmodifier"].get()) and (lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier4"])):CBStep2State[3] = lfStep2.children["cbmodifier"].get()


    # Update the display
    
    
    FillCanvasStep2(lfStep2, ModifierDict, CssTable, ButtonList, ChoiceList, ChoiceList2)
    CallConfigureCanvasStep2 = lambda event:ConfigureCanvasStep2("", lfStep2,WindowSetting)
    lfStep2.children["lfmodifier"].children["modifierworkspace"].children["canvas"].children["frame"].bind("<Configure>", CallConfigureCanvasStep2)
    lfStep2.children["lfmodifier"].children["modifierworkspace"].children["myscrollbar"].pack(side="right", fill="y")
    lfStep2.children["lfmodifier"].children["modifierworkspace"].children["canvas"].pack(side="left")
    lfStep2.children["lfmodifier"].children["modifierworkspace"].pack()
    lfStep2.children["lfmodifier"].grid(row=2, column=0, columnspan=5, sticky=" s e w")
    lfStep2.grid(row=1, column=2, sticky="n s e w")
    Bottom.grid(row=3, column=1, columnspan=3)  #move the bottom once the window enlarge
    lfStep2.children["titlestep2"].grid(row=0, column=0, columnspan=4)
    lfStep2.children["cbmodifier"].grid(row=1, column=0)
    lfStep2.children["cbviewchoice"].grid(row=1, column=1)
    lfStep2.children["cbselchoice"].grid(row=1, column=2)
    lfStep2.children["searchbar"].grid(row=1, column=3, sticky="e")
    lfStep2.children["bsearch"].grid(row=1, column=4, sticky="w")


pass

