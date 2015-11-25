from Step2.CheckbuttonExtended import*

def FillCanvasStep2(lfStep2, ModifierDict, CssTable, ButtonList, ChoiceList, ChoiceList2):

    #definition

    ModifierPerLine = 5                                     # Controls the number of modifier per line
    NameLenght = 15                                         # Controls the lenght of the Name displayed the Checkbutton
    ModifierIndex = -1                                      # CssTable line to read
    SelectionChoice = lfStep2.children["cbselchoice"].get() # Need this for treatment without modifying the value of the Combobox
    ColumnStart = 0                                         # Controls the position of the first element in grid manager
    RowStart = 0                                            # Controls the position of the first element in grid manager
    ToDisplay=[]                                            # Table storing the Checkbutton index which will be displayed

    # Apply some display settings depending on the user request such as:
    #   - The good index to read in CssTable
    #   - The number of modifier per line
    #   - the lenght of the Name displayed on the Checkbutton

    if (lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier1"]): # default Element
        ModifierIndex = 0
        ModifierPerLine = 5
        NameLenght = 22

    elif (lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier2"]):# default Class
        ModifierIndex = 1
        ModifierPerLine = 5
        NameLenght = 22

    elif (lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier3"]):# default Id
        ModifierIndex = 2
        ModifierPerLine = 5
        NameLenght = 22

    elif (lfStep2.children["cbmodifier"].get() == ModifierDict["Modifier4"]):# default At-Rule
        ModifierIndex = 3
        ModifierPerLine = 2
        NameLenght = 150

    #Clean the frame

    for i in range(0, len(ButtonList)):
        ButtonList[0].checkbutton.destroy()
        del ButtonList[0]

    #Create the CheckButtons

    for i in range(0, len(CssTable[ModifierIndex])): # for each element in the CssTable at the good index
        for j in range(0, len(CssTable[ModifierIndex][i].name)):# each name has to be displayed independently

            NewCheckButton = CheckButtonExtended(lfStep2.children["lfmodifier"].children["modifierworkspace"].children["canvas"].children["frame"],CssTable[ModifierIndex][i].name[j],NameLenght,CssTable[ModifierIndex][i].selectmode[j])
            ButtonList.append(NewCheckButton)
            
    #Apply Display settings:

    for i in range(0,len(ButtonList)):
        if (lfStep2.children["cbviewchoice"].get() == ChoiceList2[0]):
            ToDisplay.append(i)
        elif (lfStep2.children["cbviewchoice"].get() == ChoiceList2[1]):
            if((ButtonList[i].variable.get())==True):
                ToDisplay.append(i)
        elif (lfStep2.children["cbviewchoice"].get() == ChoiceList2[2]):
            if((ButtonList[i].variable.get())==False):
                ToDisplay.append(i)


    #Apply Search settings:
    if((len(lfStep2.children["searchbar"].get()))>0):
        tmp=[]
        for i in ToDisplay:
            if(str(lfStep2.children["searchbar"].get())in ButtonList[i].name):
                tmp.append(i)
        ToDisplay=tmp

    #Apply Selection settings:

    if(len(ButtonList) > 0):

        if ((SelectionChoice in ChoiceList) == False): #check that SelectionChoice is valid
            SelectionChoice = "Default"

        if (SelectionChoice == ChoiceList[0]):#None

            for i in ToDisplay:
                ButtonList[i].checkbutton.deselect()

        elif (SelectionChoice == ChoiceList[1]):# Default

            CheckbuttonIndex=0

            for i in range(0, len(ButtonList)):
                ButtonList[i].checkbutton.deselect()

            for Line in range(0, len(CssTable[ModifierIndex])):
                for NameIndex in range(0, len(CssTable[ModifierIndex][Line].name)):
                    if (CssTable[ModifierIndex][Line].nbit[NameIndex]>0):
                        ButtonList[CheckbuttonIndex].checkbutton.select()
                        CssTable[ModifierIndex][Line].selectmode[NameIndex]==True
                    CheckbuttonIndex+=1

        elif (SelectionChoice == ChoiceList[2]):#Current
            CheckbuttonIndex=0
            for Line in range(0, len(CssTable[ModifierIndex])):
                for NameIndex in range(0, len(CssTable[ModifierIndex][Line].name)):
                    if (CssTable[ModifierIndex][Line].selectmode[NameIndex] == True):
                        ButtonList[CheckbuttonIndex].checkbutton.select()
                    CheckbuttonIndex+=1

        elif (SelectionChoice == ChoiceList[3]):#All

            for i in ToDisplay:
                ButtonList[i].checkbutton.select()

        if((len(lfStep2.children["searchbar"].get()))>0):lfStep2.children["cbselchoice"].set(ChoiceList[2])

    #fill the frame inside the canvas

    Column = ColumnStart
    Row = RowStart

    for i in ToDisplay:
        if (Column==ModifierPerLine):
                Column = ColumnStart
                Row +=1
        ButtonList[i].checkbutton.grid(row=Row, column=Column, sticky="w")
        lfStep2.children["lfmodifier"].children["modifierworkspace"].children["canvas"].children["frame"].grid_columnconfigure(Column,minsize=773/ModifierPerLine)
        Column+=1

    if (len(ToDisplay)<2):
        lfStep2.children["lfmodifier"].configure(text=str(len(ToDisplay))+ " corresponding " +lfStep2.children["cbmodifier"].get() + " found in the CSS")
    elif (lfStep2.children["cbmodifier"].get()[-1]=="s"):
        lfStep2.children["lfmodifier"].configure(text=str(len(ToDisplay))+ " corresponding " +lfStep2.children["cbmodifier"].get() + "es found in the CSS")
    elif (lfStep2.children["cbmodifier"].get()[-1]=="y"):
        lfStep2.children["lfmodifier"].configure(text=str(len(ToDisplay))+ " corresponding " +lfStep2.children["cbmodifier"].get()[:-1] + "ies found in the CSS")
    else:
        lfStep2.children["lfmodifier"].configure(text=str(len(ToDisplay))+ " corresponding " +lfStep2.children["cbmodifier"].get() + "s found in the CSS")

pass
