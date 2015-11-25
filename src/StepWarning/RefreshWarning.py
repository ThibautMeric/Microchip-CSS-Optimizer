from StepWarning.FillCanvasWarning import*
from StepWarning.ConfigureCanvasWarning import*

def RefreshWarning(lfWarning, WarningList, WindowSetting):
    lfWarning.children["frame4"].pack(fill="both")
    CallConfigureCanvasWarning = lambda event : ConfigureCanvasWarning("", lfWarning, WindowSetting)
    lfWarning.children["frame4"].children["modifierworkspacewarning"].children["canvaswarning"].children["frame2"].bind("<Configure>", CallConfigureCanvasWarning)
    lfWarning.children["frame4"].children["modifierworkspacewarning"].children["myscrollbar2"].pack(side="right", fill="y")
    lfWarning.children["frame4"].children["modifierworkspacewarning"].children["canvaswarning"].pack(side="bottom")
    lfWarning.children["frame4"].children["modifierworkspacewarning"].pack(side="bottom")
    lfWarning.children["frame4"].children["topbarpack"].pack(side="top")

    lfWarning.children["frame4"].children["topbarpack"].children["titletbp"].grid(row=0, column=1)
    lfWarning.children["frame4"].children["topbarpack"].children["entryselector"].grid(row=0, column=2)
    lfWarning.children["frame4"].children["topbarpack"].children["refreshbutton"].grid(row=0, column=3)

    FillCanvasWarning(lfWarning, WarningList)

    lfWarning.grid(row=2, column=1, columnspan=10, sticky="n s e w")

pass