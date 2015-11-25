from Step1.RefreshStep1 import *

def Reset(Bottom, lfStep1, lfStep2, lfWarning, lfStep3, HtmlPath, CssPath, CssTable, HtmlTable, WarningList, CBStep2State, ModifierDict, ChoiceList2, WindowSetting):

    # re enable path modifications
    try:
        lfStep1.children["browsecss"].configure(state="active")
        lfStep1.children["browsehtml"].configure(state="active")
        lfStep1.children["read"].configure(state="active")
        lfStep1.children["entryhtml"].configure(state="active")
        lfStep1.children["entrycss"].configure(state="active")
    except:
        lfStep1.children["browsecss"].configure(state="normal")
        lfStep1.children["browsehtml"].configure(state="normal")
        lfStep1.children["read"].configure(state="normal")
        lfStep1.children["entryhtml"].configure(state="normal")
        lfStep1.children["entrycss"].configure(state="normal")

    # Reset display

    lfStep2.grid_forget()
    lfWarning.grid_forget()
    lfStep3.grid_forget()
    Bottom.grid(row=2, column=1)

    #Reset data

    for i in range(0, len(HtmlPath)):
        del HtmlPath[0]
    for i in range(0, len(CssPath)):
        del CssPath[0]
    for i in range(0, len(CssTable)):
        for y in range(0, len(CssTable[i])):
            del CssTable[i][0]
    for i in range(0, len(HtmlTable)):
        for y in range(0, len(HtmlTable[i])):
            del HtmlTable[i][0]
    for i in range(0, len(WarningList)-1):
        for y in range(0, len(WarningList[i])):
            del WarningList[i][0]

    WarningList[2].clear()

    #Reset lfstep2

    CBStep2State = ["", "", "", "", "Select?", ModifierDict["Modifier1"]]
    lfStep2.children["cbmodifier"].set(ModifierDict["Modifier1"])
    lfStep2.children["cbselchoice"].set(CBStep2State[4])
    lfStep2.children["cbviewchoice"].set(ChoiceList2[0])
    lfStep2.children["searchbar"].delete(0, END)

    #Refresh

    RefreshStep1(lfStep1, WindowSetting, HtmlPath, CssPath)

pass