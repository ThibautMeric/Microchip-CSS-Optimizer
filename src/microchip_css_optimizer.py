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
import platform
import os

    # Needed for CheckButton

        #######################
        ##GENERAL DECLARATION##
        #######################
Version = "v0.94"
HtmlPath = []                                                                           # Stores the HTML files path
CssPath = []                                                                            # Stores the CSS files path
Modifier1DataCSS = []                                                                   # Stores the CSS modifier: Element
Modifier2DataCSS = []                                                                   # Stores the CSS modifier: Class
Modifier3DataCSS = []                                                                   # Stores the CSS modifier: ID
Modifier4DataCSS = []                                                                   # Stores the CSS modifier: At-Rule
CssTable = [Modifier1DataCSS, Modifier2DataCSS, Modifier3DataCSS, Modifier4DataCSS]     # Store all the CSS data
Modifier1Name = "Element"                                                               # Name of Modifier1 (default: Element)
Modifier2Name = "Class"                                                                 # Name of Modifier1 (default: Class)
Modifier3Name = "Id"                                                                    # Name of Modifier1 (default: Id )
Modifier4Name = "At-Rule"                                                              # Name of Modifier1 (default: At-Rules)
ButtonList = []                                                                         # List of all the Checkbuttons in the frame selected or not by the user
WarningType1 = []                                                                       # List all the warning type1, Default: No CSS defintion
WarningType2 = []                                                                       # List all the warning type2, Default: Multiple CSS definiton
WarningType3 = []                                                                       # List all the warning type3, Default: CSS not oftenly used
WarningList = [WarningType1, WarningType2, WarningType3]                                  # List of all the Warnings in the warning step
Modifier1DataHTML = []                                                                  # Stores the HTML modifier: Element
Modifier2DataHTML = []                                                                  # Stores the HTML modifier: Class
Modifier3DataHTML = []                                                                  # Stores the HTML modifier: Id
HtmlTable = [Modifier1DataHTML, Modifier2DataHTML, Modifier3DataHTML]                   # Stores Store all the HTML data
CBStep2State = ["", "", "", "", "Select?", Modifier1Name]                               # Stores the state of the CBSelChoice 0:Modifier1 1:Modifier2 3:Modifier3 4:Modifier4 5:Default 6:Previous Modifier Selected

    ##############################
    ##END OF GENERAL DECLARATION##
    ##############################

        ########################
        ##FUNCTION DECLARATION##
        ########################

#Class declaration

class CssData:
    """
    Class defining a CSS Modifier Pack:
    - Type: default Element/Class/Id/At-Rules (may change depending on ModifierxName modification)
    - Name: Table with all the names of this modifier
    - Data[]:All the datas concerning this Modifier stored line after line in an array
    - NbIt: Number of iteration in the HTML file(s)
    - SelectionMode: boolean defining if the modifier will appear in the final CSS
    """

    def __init__(self, Type, Name, Data, NbIt):
        BooleanTable=[]
        for i in range(0, len(Name)):
            Boolean = BooleanVar()
            BooleanTable.append(Boolean)
        self.type = Type
        self.name = Name
        self.data = Data
        self.nbit = NbIt
        self.selectmode = BooleanTable
    pass
pass
class AtRuleData(CssData):
    """
    Class defining an AtRule Pack:
    - AtRuleData extends a classic CssData because an AtRule Modifier has a different strucutre than other CssData
    - Modifier1/Modifier2/Modifier3/Modifier4:List CssDatas included in the At_Rule (by default stored as element/id/clas/atrules)
    """

    def __init__(self, Type, Name, Data, NbIt):
        CssData.__init__(self, Type, Name, Data, NbIt)
        self.Modifier1 = []
        self.Modifier2 = []
        self.Modifier3 = []
        self.Modifier4 = []
        self.ModifierTable = [self.Modifier1,self.Modifier2,self.Modifier3,self.Modifier4]
    pass
pass
class CheckButtonExtended:
    """
    Class enlarging the definiton of Checkbuttons
    """

    def __init__(self, Name,NameLenght,Variable):
        self.checkbutton = tk.Checkbutton(frame, text=Name[:NameLenght], onvalue=True, offvalue=False, variable=Variable,command=SetCurrent)
        self.name= Name
        self.variable= Variable
    pass
pass

# Fucntion declaration
def EnableAddHtml():
    AddHtml.configure(state="active")
pass

def EnableAddCss():
    AddCss.configure(state="active")
pass

def Reset():

    # re enable path modifications
    try:
        BrowseCss.configure(state="active")
        BrowseHtml.configure(state="active")
        Read.configure(state="active")
        entryHtml.configure(state="active")
        entryCss.configure(state="active")
    except:
        BrowseCss.configure(state="normal")
        BrowseHtml.configure(state="normal")
        Read.configure(state="normal")
        entryHtml.configure(state="normal")
        entryCss.configure(state="normal")

    # Reset display

    lfStep2.grid_forget()
    lfWarning.grid_forget()
    lfStep3.grid_forget()
    Bottom.grid(row=2, column=1)

    #Reset data

    for i in range(0,len(HtmlPath)):
        del HtmlPath[0]
    for i in range(0,len(CssPath)):
        del CssPath[0]
    for i in range(0,len(CssTable)):
        for y in range(0,len(CssTable[i])):
            del CssTable[i][0]
    for i in range(0,len(HtmlTable)):
        for y in range(0,len(HtmlTable[i])):
            del HtmlTable[i][0]
    for i in range(0,len(WarningList)-1):
        for y in range(0,len(WarningList[i])):
            del WarningList[i][0]

    WarningList[2].clear()

    #Reset lfstep2

    CBStep2State = ["", "", "", "", "Select?", Modifier1Name]
    CBModifier.set(ModifierList[0])
    CBSelChoice.set(CBStep2State[4])
    CBViewChoice.set(ChoiceList2[0])
    SearchBar.delete(0,END)

    #Refresh

    RefreshStep1()

pass

def OpenCSS():
    filepath1 = askopenfilename(title="Open a file", filetypes=[('CSS files', '.css')])
    TextCss.set("")
    TextCss.set(filepath1)
    entryCss.xview_moveto(1)
    AddCss.configure(state="active")
pass

def OpenHTML():
    filepath2 = askopenfilename(title="Open a file", filetypes=[('HTML files', '.html')])
    TextHtml.set("")
    TextHtml.set(filepath2)
    entryHtml.xview_moveto(1)
    AddHtml.configure(state="active")
pass

def AddCSS():
    CssPath.append(entryCss.get())
    RefreshStep1()
    AddCss.configure(state="disabled")
    if(len(HtmlPath)>0):
        Read.grid(row=len(CssPath) + len(HtmlPath) + 9, column=0, pady="5")
pass

def AddHTML():
    HtmlPath.append(entryHtml.get())
    RefreshStep1()
    AddHtml.configure(state="disabled")
    Read.grid(row=len(CssPath) + len(HtmlPath) + 9, column=0, pady="5")

pass
def SetCurrent():
    CBSelChoice.set(ChoiceList[2])
    CBStep2State[ModifierList.index(CBModifier.get())]=CBSelChoice.get()
pass
def IsDotMin():
    GenerateCss(1)
pass
def IsClassic():
    GenerateCss(0)
pass
def GenerateCss(Type):
    IS_CLASSIC=0
    IS_DOT_MIN=1
    FileContent="/*Generated by Microchip CSS Optimizer " + Version +"*/\n"

    #Insert in the file Modifier 1-2-3

    for ColumnInCss in range(0,len(CssTable)-1):                                  # define position in CSS table
        for LineInCss in range(0,len(CssTable[ColumnInCss])):
            IndexToAdd=[]

            for NameIndex in range(0,len(CssTable[ColumnInCss][LineInCss].name)): # get names used
                if (CssTable[ColumnInCss][LineInCss].selectmode[NameIndex].get()==True):
                    IndexToAdd.append(NameIndex)

            for i in IndexToAdd:                                                  # print names used
                FileContent+=CssTable[ColumnInCss][LineInCss].name[i]
                if(IndexToAdd.index(i)<len(IndexToAdd)-1):
                    FileContent+=(",")
                FileContent+="\n"

            if(len(IndexToAdd)>0):                                                # print data
                Index = []
                for i in range(0,len(CssTable[ColumnInCss][LineInCss].data)):
                    if ((CssTable[ColumnInCss][LineInCss].data[i]==";")or (CssTable[ColumnInCss][LineInCss].data[i]=="{")):
                        Index.append(i+1)
                tmp=list(CssTable[ColumnInCss][LineInCss].data)
                y=0
                for i in range(0,len(Index)):
                    tmp.insert(Index[i]+y,"\n")
                    y+=1
                FileContent+=''.join(tmp) + " "
                FileContent+="\n"

    #Insert in the file Modifier 4, default At-Rule

    ColumnInCss=3                                                                 # define position in CSS table
    for LineInCss in range(0,len(CssTable[ColumnInCss])):

        if(CssTable[ColumnInCss][LineInCss].selectmode[0].get()==True):
            AtRuleTable=CssTable[ColumnInCss][LineInCss].ModifierTable
            IndexToAdd=[]
            FileContent +=CssTable[ColumnInCss][LineInCss].name[0] +"\n" + "{" + "\n"
            for ColumnInAtRule in range(0,len(AtRuleTable)):                      # define position in AtRule
                for LineInAtRule in range(0,len(AtRuleTable[ColumnInAtRule])):

                    for NameIndex in range(0,len(AtRuleTable[ColumnInAtRule][LineInAtRule].name)): # get names used

                        if (AtRuleTable[ColumnInAtRule][LineInAtRule].nbit[NameIndex]>0):

                            IndexToAdd.append(NameIndex)


                    if((CssTable[ColumnInCss][LineInCss].selectmode[0].get()==True)and(CssTable[ColumnInCss][LineInCss].nbit[0]==0)):# Handle case user wants the At-Rule even if not used

                        for NameIndex in range(0,len(AtRuleTable[ColumnInAtRule][LineInAtRule].name)): # get names used
                            IndexToAdd.append(NameIndex)



                    for i in IndexToAdd:                                                   # print names used
                        FileContent+= "\t" + AtRuleTable[ColumnInAtRule][LineInAtRule].name[i]
                        if(i<len(IndexToAdd)-1):
                            FileContent+=(",")
                        FileContent+="\n"


                    if(len(IndexToAdd)>0):                                                # print data
                        FileContent+="\t"
                        Index = []

                        for i in range(0,len(AtRuleTable[ColumnInAtRule][LineInAtRule].data)):
                            if ((AtRuleTable[ColumnInAtRule][LineInAtRule].data[i]==";")or (AtRuleTable[ColumnInAtRule][LineInAtRule].data[i]=="{")):
                                    while(AtRuleTable[ColumnInAtRule][LineInAtRule].data[i+1]==" "):
                                        i+=1
                                    Index.append(i)

                        temp = AtRuleTable[ColumnInAtRule][LineInAtRule].data
                        temp = temp.replace("  ", " ")
                        temp = temp.replace("   ", " ")
                        temp = temp.replace("    ", " ")
                        tmp=list(temp)
                        for i in range(0,len(Index)):
                            tmp.insert(int(Index[i]),"\n\t")

                        FileContent+=''.join(tmp)
                        FileContent+="\n"
                    IndexToAdd[:] = []
            FileContent +="}\n"


    if (Type==IS_DOT_MIN):
        FileContent = FileContent.replace('\n', '')
        FileContent = FileContent.replace('\t', '')
        FileContent = FileContent.replace("  ", " ")
        FileContent = FileContent.replace("   ", " ")
        FileContent = FileContent.replace("    ", "")

        SaveAs = asksaveasfile(mode='w', defaultextension="",title="Save As:", filetypes=[('min CSS files', '.min.css')])
        if SaveAs is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        name= SaveAs.name
        if SaveAs.name[(len(SaveAs.name)-8):]!=".min.css":
            os.rename(SaveAs.name,SaveAs.name +".min.css")
            name+=".min.css"
        SaveAs.write(FileContent)
        SaveAs.close()
        try:
            tkinter.messagebox.showinfo("Generation successful","Your file was successfully generated under:\n"+name)
        except:
            tkMessageBox.showinfo("Generation successful","Your file was successfully generated under:\n"+name)

    else:
        SaveAs = asksaveasfile(mode='w', defaultextension="",title="Save As:", filetypes=[('CSS files', '.css')])
        if SaveAs is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        name= SaveAs.name
        if SaveAs.name[(len(SaveAs.name)-4):]!=".css":
            os.rename(SaveAs.name,SaveAs.name +".css")
            name+=".css"
        SaveAs.write(FileContent)
        SaveAs.close()
        try:
            tkinter.messagebox.showinfo("Generation successful","Your file was successfully generated under:\n"+name)
        except:
            tkMessageBox.showinfo("Generation successful","Your file was successfully generated under:\n"+name)




pass

def FillCanvasStep2():

    #definition

    ModifierPerLine = 5                   # Controls the number of modifier per line
    NameLenght = 15                       # Controls the lenght of the Name displayed the Checkbutton
    ModifierIndex = -1                    # CssTable line to read
    SelectionChoice = CBSelChoice.get()   # Need this for treatment without modifying the value of the Combobox
    ColumnStart = 0                       # Controls the position of the first element in grid manager
    RowStart = 0                          # Controls the position of the first element in grid manager
    ToDisplay=[]                          # Table storing the Checkbutton index which will be displayed

    # Apply some display settings depending on the user request such as:
    #   - The good index to read in CssTable
    #   - The number of modifier per line
    #   - the lenght of the Name displayed on the Checkbutton

    if (CBModifier.get() == Modifier1Name): # default Element
        ModifierIndex = 0
        ModifierPerLine = 5
        NameLenght = 22

    elif (CBModifier.get() == Modifier2Name):# default Class
        ModifierIndex = 1
        ModifierPerLine = 5
        NameLenght = 22

    elif (CBModifier.get() == Modifier3Name):# default Id
        ModifierIndex = 2
        ModifierPerLine = 5
        NameLenght = 22

    elif (CBModifier.get() == Modifier4Name):# default At-Rule
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

            NewCheckButton = CheckButtonExtended(CssTable[ModifierIndex][i].name[j],NameLenght,CssTable[ModifierIndex][i].selectmode[j])
            ButtonList.append(NewCheckButton)

    #Apply Display settings:

    for i in range(0,len(ButtonList)):
        if (CBViewChoice.get() == ChoiceList2[0]):
            ToDisplay.append(i)
        elif (CBViewChoice.get() == ChoiceList2[1]):
            if((ButtonList[i].variable.get())==True):
                ToDisplay.append(i)
        elif (CBViewChoice.get() == ChoiceList2[2]):
            if((ButtonList[i].variable.get())==False):
                ToDisplay.append(i)


    #Apply Search settings:
    if((len(SearchBar.get()))>0):
        tmp=[]
        for i in ToDisplay:
            if(str(SearchBar.get())in ButtonList[i].name):
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

        if((len(SearchBar.get()))>0):CBSelChoice.set(ChoiceList[2])

    #fill the frame inside the canvas

    Column = ColumnStart
    Row = RowStart

    for i in ToDisplay:
        if (Column==ModifierPerLine):
                Column = ColumnStart
                Row +=1
        ButtonList[i].checkbutton.grid(row=Row, column=Column, sticky="w")
        frame.grid_columnconfigure(Column,minsize=(frame.winfo_width()/ModifierPerLine))
        Column+=1

    if (len(ToDisplay)<2):
        lfModifier.configure(text=str(len(ToDisplay))+ " corresponding " +CBModifier.get() + " found in the CSS")
    elif (CBModifier.get()[-1]=="s"):
        lfModifier.configure(text=str(len(ToDisplay))+ " corresponding " +CBModifier.get() + "es found in the CSS")
    elif (CBModifier.get()[-1]=="y"):
        lfModifier.configure(text=str(len(ToDisplay))+ " corresponding " +CBModifier.get()[:-1] + "ies found in the CSS")
    else:
        lfModifier.configure(text=str(len(ToDisplay))+ " corresponding " +CBModifier.get() + "s found in the CSS")

pass
def FillCanvasWarning():
    DisplayWarning1 = []
    DisplayWarning2 = []
    DisplayWarning3 = []
    Display = [DisplayWarning1,DisplayWarning2,DisplayWarning3]
    tmp=[]
    HideContainingX = []
    HideNamedX = []
    Displaymodifier = [HideContainingX,HideNamedX]
    tmp2 = ""
    tmp2 = ''.join(map(str,EntrySelector.get()))

   #Get the elements not to show

    for i in range(0,len(tmp2.split(' '))):
        tmp.insert(int(i),tmp2.split(' ')[i])

    for index in range(0,len(tmp)):
        if (str(tmp[index]).find("*")>0):
            Displaymodifier[0].append(tmp[index].replace('*', ''))
        else:
            Displaymodifier[1].append(tmp[index])

    #Error No CSS files: Check if displayed or not

    for index in range(0,len(WarningList[0])):
        InNoContaining = 0
        InNoNamed = 0
        for i in range(0,len(HideContainingX)):

            if ((WarningList[0][index].find(HideContainingX[i]))>-1):

                InNoContaining = 1

        for k in range(0,len(HideNamedX)):
            if (HideNamedX[k] == WarningList[0][index]):
                InNoNamed = 1

        if(InNoContaining+InNoNamed==0):
            string =str(WarningList[0][index]) +" is not defined in any of the selected CSS files"
            Display[0].append(string)

     #Error Defined multiple times: Check if displayed or not

    for index in range(0,len(WarningList[1])):
        InNoContaining = 0
        InNoNamed = 0
        for i in range(0,len(HideContainingX)):
            if ((WarningList[1][index].find(HideContainingX[i]))>-1):
                InNoContaining = 1

        for k in range(0,len(HideNamedX)):
            if (HideNamedX[k] == WarningList[1][index]):
                InNoNamed = 1

        if(InNoContaining+InNoNamed==0):
            string = str(WarningList[1][index]) + " is defined more than one time, compress it in one definiton may lighten your CSS file"
            Display[1].append(string)

    #Error not oftenly used: Check if displayed or not
    if(len(WarningList[2])>0):
        for key,Iteration in WarningList[2].items():
            InNoContaining = 0
            InNoNamed = 0
            for i in range(0,len(HideContainingX)):
                if ((key.find(HideContainingX[i]))>-1):
                    InNoContaining = 1

            for k in range(0,len(HideNamedX)):
                if (HideNamedX[k] == key):
                    InNoNamed = 1

            if(InNoContaining+InNoNamed==0):
                string = "{} is only used {} time(s), removing it's definiton may lighten your CSS file".format(key,Iteration)
                Display[2].append(string)

    #Clean the frame

    for widget in frame2.winfo_children():
        widget.destroy()

    #Display the number of errors

    ModifierWorkspaceWarning.configure(text=str(len(Display[0])+len(Display[1])+len(Display[2])) + " warning(s):")

    #label = tk.Label(frame2, text=str(len(Display[0])+len(Display[1])+len(Display[2])) + " warning(s):", fg="red")
    #label.grid(row=1, column=0, sticky="w")

    #Display the Warnings

    Column = 1
    Row = 1
    MaxColumn=2

    for index in range (0,len(Display)):
        Column = 1
        for i in range(1,len(Display[index])+1):

            label = tk.Label(frame2, text=Display[index][i-1], fg="red")
            label.grid(row=Row, column=Column, sticky="w",padx=5, pady=5)
            Column+=1
            if (Column>MaxColumn):
               Column = 1
               Row +=1
        if(index+1<len(Display)):
            if (len(Display[index+1])>0):
                Row +=1
                label = tk.Label(frame2, text="------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", fg="red")
                label.grid(row=Row, column=1,columnspan=2, pady=5, sticky="w")
                Row +=1


pass

def ConfigureCanvasStep2(event):
    WidthCBModifier = 750*coefwindow
    HeightCBModifier = 220*coefwindow
    canvas.configure(scrollregion=canvas.bbox("all"), width=WidthCBModifier, height=HeightCBModifier)
pass
def ConfigureCanvasWarning(event):
    WidthWarning = 1200*coefwindow
    HeightWarning = 300*coefwindow
    CanvasWarning.configure(scrollregion=CanvasWarning.bbox("all"), width=WidthWarning, height=HeightWarning)
pass

def RefreshStep1():
    NB_HTML = len(HtmlPath)                               # Number of HTML files selected
    NB_CSS = len(CssPath)                                 # Number of CSS files selected

    #Clean the frame

    for widget in lfStep1.winfo_children():
        widget.grid_forget()


    line =0
    TitleCss.grid(row=0, column=0, pady="5")
    line+=1
    for i in range(0,NB_CSS):
        NewLabel = Label(lfStep1, text="..." + CssPath[i][int(-40*coef):])
        NewLabel.grid(row=line, column=0)
        line+=1
    TextCss.set("Insert Path")
    entryCss.grid(row=line, column=0, pady="5")
    BrowseCss.grid(row=line, column=1, pady="5")
    line+=1
    AddCss.grid(row=line, column=0, pady="5")
    line+=1


    TitleHtml.grid(row=line, column=0, pady="5")
    line+=1
    for i in range(0,NB_HTML):
        NewLabel = Label(lfStep1, text="..." + HtmlPath[i][int(-40*coef):])
        NewLabel.grid(row=line, column=0)
        line+=1
    TextHtml.set("Insert Path")
    entryHtml.grid(row=line, column=0, pady="5")
    BrowseHtml.grid(row=line, column=1, pady="5")
    line+=1
    AddHtml.grid(row=line, column=0, pady="5")

    lfStep1.grid(row=1, column=1, sticky="n s e w")
pass

def RefreshStep2(event):

    # if change Modifier Group Selection

    if(CBStep2State[5] != CBModifier.get()):

        #Apply the corresponding selection setting (none/default/current/all) when Modifier group is changed by the user

        if(CBModifier.get() == Modifier1Name):# Default: if Element
            if(CBStep2State[0] != ""):CBSelChoice.set(CBStep2State[0])
            else:CBSelChoice.set(CBStep2State[4])
        elif(CBModifier.get() == Modifier2Name):# Default: if Class
            if(CBStep2State[1] != ""):CBSelChoice.set(CBStep2State[1])
            else:CBSelChoice.set(CBStep2State[4])
        elif(CBModifier.get() == Modifier3Name):# Default: if Id
            if(CBStep2State[2] != ""):CBSelChoice.set(CBStep2State[2])
            else:CBSelChoice.set(CBStep2State[4])
        elif(CBModifier.get() == Modifier4Name):# Default: if At-rules
            if(CBStep2State[3] != ""):CBSelChoice.set(CBStep2State[3])
            else:CBSelChoice.set(CBStep2State[4])

        CBStep2State[5] = CBModifier.get()

    # if change Selection Mode

    else:
        if((CBStep2State[0] != CBSelChoice.get()) and (CBModifier.get() == Modifier1Name)):CBStep2State[0] = CBSelChoice.get()
        elif((CBStep2State[1] != CBSelChoice.get()) and (CBModifier.get() == Modifier2Name)):CBStep2State[1] = CBSelChoice.get()
        elif((CBStep2State[2] != CBSelChoice.get()) and (CBModifier.get() == Modifier3Name)):CBStep2State[2] = CBSelChoice.get()
        elif((CBStep2State[3] != CBSelChoice.get()) and (CBModifier.get() == Modifier4Name)):CBStep2State[3] = CBSelChoice.get()


    # Update the display

    FillCanvasStep2()
    frame.bind("<Configure>", ConfigureCanvasStep2)
    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    ModifierWorkspace.pack()
    lfModifier.grid(row=2, column=0, columnspan=3, sticky=" s e w")
    lfStep2.grid(row=1, column=2, sticky="n s e w")
    Bottom.grid(row=3, column=1, columnspan=3)  #move the bottom once the window enlarge
    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    lfModifier.grid(row=2, column=0, columnspan=5, sticky=" s e w")
    TitleStep2.grid(row=0, column=0, columnspan=4)
    CBModifier.grid(row=1, column=0)
    CBViewChoice.grid(row=1, column=1)
    CBSelChoice.grid(row=1, column=2)
    SearchBar.grid(row=1, column=3, sticky="e")
    BSearch.grid(row=1, column=4, sticky="w")
pass

def RefreshWarning():
    frame4.pack(fill="both")
    #WidthWarning = 1200
    #HeightWarning = 200
    frame2.bind("<Configure>", ConfigureCanvasWarning)
    myscrollbar2.pack(side="right", fill="y")
    CanvasWarning.pack(side="bottom")
    ModifierWorkspaceWarning.pack(side="bottom")
    TopBarPack.pack(side="top")

    TitleTBP.grid(row=0, column=1)
    EntrySelector.grid(row=0, column=2)
    RefreshButton.grid(row=0, column=3)

    FillCanvasWarning()


    lfWarning.grid(row=2, column=1, columnspan=10, sticky="n s e w")

pass

def RefreshStep3():

    Generate.grid(row=0, column=0, pady="30")
    GenerateDotMin.grid(row=1, column=0, pady="30")
    Reset.grid(row=2, column=0, pady="30")
    lfStep3.grid(row=1, column=3, sticky="n s")

pass

def GetWindowData(g):
    r = [i for i in range(0, len(g)) if not g[i].isdigit()]
    return [int(g[0:r[0]]), int(g[r[0] + 1:r[1]]), int(g[r[1] + 1:r[2]]), int(g[r[2] + 1:])]

pass

def ReadFile():

    #Unexpected action handler

    if(len(CssPath)==0):
        try:
            tkinter.messagebox.showerror ("Error: No CSS","Please add a CSS file")
        except:
            tkMessageBox.showerror ("Error: No CSS","Please add a CSS file")
        return
    elif(len(HtmlPath)==0):
        try:
            tkinter.messagebox.showerror ("Error: No HTML","Please add an HTML file")
        except:
            tkMessageBox.showerror ("Error: No HTML","Please add an HTML file")
        return
    else:

        Error="The following files are unvalid:"
        DefaultErrorLenght=len(Error)
        RemoveCss=[]
        RemoveHtml=[]
        for i in range(0,len(CssPath)):
            if(os.path.isfile(str(CssPath[i]))==False):
                Error+="\n..."+CssPath[i][-40:]+": Not Found"+"\n"
                RemoveCss.append(i)
        for i in RemoveCss[::-1]:
            CssPath.remove(CssPath[i])
        RemoveCss=[]

        for i in range(0,len(HtmlPath)):
            if(os.path.isfile(str(HtmlPath[i]))==False):
                Error+="\n..."+HtmlPath[i][-40:]+": Not Found"+"\n"
                RemoveHtml.append(i)
        for i in RemoveHtml[::-1]:
            HtmlPath.remove(HtmlPath[i])
        RemoveHtml=[]

        for i in range(0,len(CssPath)):
            if(CssPath[i][-4]!="." or CssPath[i][-3]!="c" or CssPath[i][-2]!="s" or CssPath[i][-1]!="s"):
                Error+="\n..."+CssPath[i][-40:] +": Not CSS"+"\n"
                RemoveCss.append(i)
        for i in RemoveCss[::-1]:
            CssPath.remove(CssPath[i])
        RemoveCss=[]

        for i in range(0,len(HtmlPath)):
            if(HtmlPath[i][-5]!="." or HtmlPath[i][-4]!="h" or HtmlPath[i][-3]!="t" or HtmlPath[i][-2]!="m" or HtmlPath[i][-1]!="l"):
                Error+="\n..."+HtmlPath[i][-40:]+": Not HTML"+"\n"
                RemoveHtml.append(i)
        for i in RemoveHtml[::-1]:
            HtmlPath.remove(HtmlPath[i])
        RemoveHtml=[]

        for i in range(0,len(CssPath)):
            if(CssPath.count(CssPath[i])>1):
                Error+="\n..."+CssPath[i][-40:]+": Found Multiple times"+"\n"
                RemoveCss.append(i)

        for i in RemoveCss[::-1]:
            del CssPath[i]
        RemoveCss=[]

        for i in range(0,len(HtmlPath)):
            if(HtmlPath.count(HtmlPath[i])>1):
                Error+="\n..."+HtmlPath[i][-40:]+": Found Multiple times"+"\n"
                RemoveHtml.append(i)

        for i in RemoveHtml[::-1]:
            del HtmlPath[i]
        RemoveHtml=[]

        if(len(Error)>DefaultErrorLenght):
            try:
                tkinter.messagebox.showerror ("Error: Incorrect File(s)",Error)
            except:
                tkMessageBox.showerror ("Error: Incorrect File(s)",Error)
            RefreshStep1()
            Read.grid(row=len(CssPath) + len(HtmlPath) + 9, column=0, pady="5")
            return


    # Disable path modifications

    BrowseCss.configure(state="disabled")
    BrowseHtml.configure(state="disabled")
    Read.configure(state="disabled")
    entryHtml.configure(state="disabled")
    entryCss.configure(state="disabled")

    #Read the files

    ReadCSS()
    ReadHTML()
    Optimize()

    #Display Step 2

    RefreshStep2("")

    #Display warning

    RefreshWarning()

    #Display Step 3

    RefreshStep3()

    # Move the window to the center of the screen
    """
    Window.update_idletasks()
    Window.state('zoomed')
    X= Window.winfo_width()
    Y= Window.winfo_height()
    Window.state('normal')
    w,h,x,y=GetWindowData(Window.geometry())
    Window.geometry("%dx%d%+d%+d" % (w,h,((X-w)//2)-50,10))
    """

pass

def ReadHTML():
    for i in range(0, len(HtmlPath)):                        #Reads all the HTML files
        HtmlFile = open(HtmlPath[i], "r")
        Data = HtmlFile.read()
        HtmlFile.close
        Data = Data.replace('\n', '')
        Data = Data.replace('\t', '')
        Data = Data.replace("  ", " ")
        Data = Data.replace("   ", " ")
        Data = Data.replace("    ", "")

        while(len(Data) > 0):                                #Current file treatment loop

            if(Data[0] == '<' and Data[1] == '!' and Data[2] == '-' and Data[3] == '-'):#delete the comments
                while(1):
                    if (Data[0] == '-' and Data[1] == '-' and Data[2] == '>'):
                        break
                    else:Data = Data[1:]

            elif (Data[0] == "<" and Data[1] != "/"):#if an HTML tag is found
                tmpdata = []
                Data = Data[1:]# delete < from name
                while(Data[0] != ' ' and Data[0] != '>'):# get tag name
                    tmpdata.append(Data[0])
                    Data = Data[1:]
                HtmlTable[0].append(''.join(tmpdata))

                while(Data[0] != '>'):                       #as long as the tag is not fully read
                    tmpdata = []


                    if(Data[0] == 'c' and Data[1] == 'l' and Data[2] == 'a' and Data[3] == 's' and Data[4] == 's'and (Data[5] == " "or Data[5] == "=")):#if class tag is found
                        while(Data[0] != '"'):#push inside the class definiton to get data
                            Data = Data[1:]
                        Data = Data[1:]
                        while(1):# while inside Class definition
                            if(Data[0] == ' '):
                                Data = Data[1:]
                                if (len(tmpdata) > 0):
                                    HtmlTable[1].append("."+''.join(tmpdata))# add to the table
                                    tmpdata = []
                            if(Data[0] == '"'):# if reading is over
                                Data = Data[1:]
                                if (len(tmpdata) > 0):
                                    HtmlTable[1].append("."+''.join(tmpdata))# add to the table
                                    tmpdata = []
                                break
                            else:#get the class name
                                tmpdata.append(Data[0])
                                Data = Data[1:]
                        Data = Data[1:]

                    elif(Data[0] == 'i' and Data[1] == 'd'and (Data[2] == " "or Data[2] == "=")):#if id tag is found
                        while(Data[0] != '"'):#push inside the id definiton to get data
                            Data = Data[1:]
                        Data = Data[1:]

                        while(1):# while inside Id definition
                            if(Data[0] == ' '):
                                Data = Data[1:]
                                if (len(tmpdata) > 0):
                                    HtmlTable[2].append("#"+''.join(tmpdata))# add to the table
                                    tmpdata = []
                            if(Data[0] == '"'):# if reading is over
                                Data = Data[1:]
                                if (len(tmpdata) > 0):
                                    HtmlTable[2].append("#"+''.join(tmpdata))# add to the table
                                    tmpdata = []
                                break
                            else:#get the class name
                                tmpdata.append(Data[0])
                                Data = Data[1:]
                        Data = Data[1:]

                    elif(Data[0] == '"'):# prevent misinterpretation when "id" or "class" is included in a definition
                        Data = Data[1:]
                        while(Data[0] != '"'):
                            Data = Data[1:]
                        Data = Data[1:]
                    else:Data = Data[1:]

            elif(Data[0] == 'f' and Data[1] == 'u' and Data[2] == 'n' and Data[3] == 'c' and Data[4] == 't' and Data[5] == 'i'and Data[6] == 'o'and Data[7] == 'n'):
                flag = 0
                while(Data[0] != '{'):#push inside the id tag to get data
                    Data = Data[1:]
                Data = Data[1:]
                flag += 1
                while(flag == 0):#delete the function
                    if (Data[0] == '{'):flag += 1
                    if (Data[0] == '}'):flag -= 1



            else:Data = Data[1:]

pass

def ReadCSS():

    for i in range(0, len(CssPath)):                        # Reads all the CSS files

        CssFile = open(CssPath[i], "r")
        Data = CssFile.read()
        CssFile.close
        Data = Data.replace('\n', '')
        Data = Data.replace('\t', '')
        Data = Data.replace("  ", " ")
        Data = Data.replace("   ", " ")

        while(len(Data) > 0):                                # Current file treatment loop
            NameNewCssData = []
            DataNewCssData = []
            NameTable = []
            if(Data[0] == '/' and Data[1] == '*'):           # delete the comments
                while(Data[0] != '*' or Data[1] != '/'):
                    Data = Data[1:]
                Data = Data[1:]
                Data = Data[1:]

            elif (Data[0] == "@"):                           # this is an At-Rule
                NbBraceOp = 1

                while(True):#get the name of the Rule
                    NameNewCssData += Data[0]
                    Data = Data[1:]
                    if(len(Data) == 0):
                        break
                    if (Data[0] == "{"):
                        break

                NewAtRule = AtRuleData(Modifier4Name, [''.join(NameNewCssData)], "", [0])

                while(NbBraceOp > 0):#get modifiers inside the At-Rule
                    NameNewCssDataForAtRule = []
                    DataNewCssDataForAtRule = []
                    Data = Data[1:]
                    NameTable = []
                    while(True):#get name of elements inside the rule
                        NameNewCssDataForAtRule += Data[0]
                        Data = Data[1:]

                        if(len(Data) == 0):
                            break
                        if (Data[0] == "}"):
                            NameTable.append(''.join(NameNewCssDataForAtRule).strip())
                            NbBraceOp -= 1
                            break
                        if (Data[0] == "{"):
                            NameTable.append(''.join(NameNewCssDataForAtRule).strip())
                            NbBraceOp += 1
                            break
                        if (Data[0] == ","):
                            NameTable.append(''.join(NameNewCssDataForAtRule).strip())
                            Data = Data[1:]
                            NameNewCssDataForAtRule = []

                    while(True):#getdata
                        DataNewCssDataForAtRule += Data[0]
                        if (Data[0] == "}"):
                            Data = Data[1:]
                            NbBraceOp -= 1
                            break

                        Data = Data[1:]

                    if(( "@" in str(NameTable)) == True):AddToTable(NewAtRule.ModifierTable[3], NameTable, DataNewCssDataForAtRule)
                    elif(( "#" in str(NameTable)) == True):AddToTable(NewAtRule.ModifierTable[2], NameTable, DataNewCssDataForAtRule)
                    elif(( "." in str(NameTable)) == True):AddToTable(NewAtRule.ModifierTable[1], NameTable, DataNewCssDataForAtRule)
                    else:AddToTable(NewAtRule.ModifierTable[0], NameTable, DataNewCssDataForAtRule)

                    if (Data[0] == "}"): # Check if the At-Rule is over
                        NbBraceOp -= 1

                CssTable[3].append(NewAtRule)
            elif (Data[0] == " " or Data[0] == "}"):
                Data = Data[1:]
            else:                             # this is an Element or Class or Id
                while(True):#getname
                    NameNewCssData += Data[0]
                    Data = Data[1:]
                    if(len(Data) == 0):
                        break
                    if (Data[0] == "{"):
                        NameTable.append(''.join(NameNewCssData).strip())
                        break
                    if (Data[0] == ","):
                        NameTable.append(''.join(NameNewCssData).strip())
                        Data = Data[1:]
                        NameNewCssData = []

                if(len(Data) != 0):
                    while(True):#getdata
                        DataNewCssData += Data[0]
                        if (Data[0] == "}"):
                            Data = Data[1:]
                            break
                        Data = Data[1:]

                    if(( "#" in NameTable[0]) == True):
                        AddToTable(CssTable[2], NameTable, DataNewCssData)
                    elif(( "." in NameTable[0]) == True):
                        AddToTable(CssTable[1], NameTable, DataNewCssData)
                    else:
                        AddToTable(CssTable[0], NameTable, DataNewCssData)

pass
def Optimize():
    global NbCss
    global WarningList
    Defined = []
    FoundMultipleTime = []
    NotDefined = []
    NotUsedOftenly = {}
    FOUND=0
    NOT_FOUND=1
    FUND_MULTIPLE_TIME=2
    NOT_OFTENLY_FOUND=3
    Case=[Defined,NotDefined,FoundMultipleTime,NotUsedOftenly]
    M1DataHTMLReduced = list(set(HtmlTable[0]))
    M2DataHTMLReduced = list(set(HtmlTable[1]))
    M3DataHTMLReduced = list(set(HtmlTable[2]))
    HtmlTableReduced = [M1DataHTMLReduced, M2DataHTMLReduced, M3DataHTMLReduced]
    M1NBIT = []
    M2NBIT = []
    M3NBIT = []
    NbItTable = [M1NBIT,M2NBIT,M3NBIT]

    #Get NbIt

    for ColumnInHtml in range(0,len(HtmlTable)):                                        # define position in HTML table
        for LineInHtmlReduced in range(0,len(HtmlTableReduced[ColumnInHtml])):
            NbItTable[ColumnInHtml].append(HtmlTable[ColumnInHtml].count(HtmlTableReduced[ColumnInHtml][LineInHtmlReduced]))

    #Check in Column 1-2-3 in CssTable

    for ColumnInHtml in range(0,len(HtmlTableReduced)):                                    # define position in HTML table
        for LineInHtml in range(0,len(HtmlTableReduced[ColumnInHtml])):

            ColumnInCss = ColumnInHtml                                              # define position in CSS table
            for LineInCss in range(0,len(CssTable[ColumnInCss])):

                if(HtmlTableReduced[ColumnInHtml][LineInHtml] in CssTable[ColumnInCss][LineInCss].name):

                    CssTable[ColumnInCss][LineInCss].nbit[CssTable[ColumnInCss][LineInCss].name.index(HtmlTableReduced[ColumnInHtml][LineInHtml])]=NbItTable[ColumnInHtml][LineInHtml]
                    CssTable[ColumnInCss][LineInCss].selectmode[CssTable[ColumnInCss][LineInCss].name.index(HtmlTableReduced[ColumnInHtml][LineInHtml])].set(True)

                    if((HtmlTableReduced[ColumnInHtml][LineInHtml] in Case[FOUND]) ==False):
                        Case[FOUND].append(HtmlTableReduced[ColumnInHtml][LineInHtml])
                    elif((HtmlTableReduced[ColumnInHtml][LineInHtml] in Case[FUND_MULTIPLE_TIME])==False):
                        Case[FUND_MULTIPLE_TIME].append(HtmlTableReduced[ColumnInHtml][LineInHtml])


            if((HtmlTableReduced[ColumnInHtml][LineInHtml] in Case[NOT_FOUND])==False):
                if((HtmlTableReduced[ColumnInHtml][LineInHtml] in Case[FOUND])== False):
                    Case[NOT_FOUND].append(HtmlTableReduced[ColumnInHtml][LineInHtml])


    #Check if modifier is common

    for column in range(0,len(CssTable)): #check modifier1 table then modifier2 table and then modifier3 table
        for line in range(0,len(CssTable[column])):# reads all the htmlTable

            for NbItIndex in range(0,len(CssTable[column][line].nbit)):
                if(CssTable[column][line].nbit[NbItIndex] <=(2*len(HtmlPath))and CssTable[column][line].nbit[NbItIndex]>0):

                    tmp=""
                    tmp+= CssTable[column][line].name[NbItIndex]
                    Case[NOT_OFTENLY_FOUND][tmp] =  str(CssTable[column][line].nbit[NbItIndex])

    #Check in Column 4 in CssTable

    for ColumnInHtml in range(0,len(HtmlTableReduced)):                                    # define position in HTML table
        for LineInHtml in range(0,len(HtmlTableReduced[ColumnInHtml])):

            ColumnInCss = 3                                                         # define position in CSS table
            for LineInCss in range(0,len(CssTable[ColumnInCss])):

                ColumnInAtRule = ColumnInHtml                                       # define position in AtRule
                for LineInAtRule in range(0,len(CssTable[ColumnInCss][LineInCss].ModifierTable[ColumnInAtRule])):

                    if(HtmlTableReduced[ColumnInHtml][LineInHtml] in CssTable[ColumnInCss][LineInCss].ModifierTable[ColumnInAtRule][LineInAtRule].name):

                        CssTable[ColumnInCss][LineInCss].ModifierTable[ColumnInAtRule][LineInAtRule].nbit[CssTable[ColumnInCss][LineInCss].ModifierTable[ColumnInAtRule][LineInAtRule].name.index(HtmlTableReduced[ColumnInHtml][LineInHtml])]=NbItTable[ColumnInHtml][LineInHtml]
                        CssTable[ColumnInCss][LineInCss].ModifierTable[ColumnInAtRule][LineInAtRule].selectmode[CssTable[ColumnInCss][LineInCss].ModifierTable[ColumnInAtRule][LineInAtRule].name.index(HtmlTableReduced[ColumnInHtml][LineInHtml])].set(True)
                        CssTable[ColumnInCss][LineInCss].nbit[0]+=1
                        CssTable[ColumnInCss][LineInCss].selectmode[0].set(True)

                        if((HtmlTableReduced[ColumnInHtml][LineInHtml] in Case[FOUND]) ==False):
                            Case[FOUND].append(HtmlTableReduced[ColumnInHtml][LineInHtml])
                        elif((HtmlTableReduced[ColumnInHtml][LineInHtml] in Case[FUND_MULTIPLE_TIME])==False):
                            Case[FUND_MULTIPLE_TIME].append(HtmlTableReduced[ColumnInHtml][LineInHtml])
                        if((HtmlTableReduced[ColumnInHtml][LineInHtml] in Case[NOT_FOUND])):
                            Case[NOT_FOUND].remove(HtmlTableReduced[ColumnInHtml][LineInHtml])

            if ((HtmlTableReduced[ColumnInHtml][LineInHtml] in Case[FOUND]) ==False):
                if((HtmlTableReduced[ColumnInHtml][LineInHtml] in Case[NOT_FOUND])== False):
                    Case[NOT_FOUND].append(HtmlTableReduced[ColumnInHtml][LineInHtml])


    #Check if modifier is common

    ColumnInCss = 3                                                                           # define position in CSS file
    for LineInCss in range(0,len(CssTable[ColumnInCss])):

        for ColumnInAtRule in range(0,len(CssTable[ColumnInCss][LineInCss].ModifierTable)):   # define position in AtRule
            for LineInAtRule in range(0,len(CssTable[ColumnInCss][LineInCss].ModifierTable[ColumnInAtRule])):

                for NbItIndex in range(0,len(CssTable[ColumnInCss][LineInCss].nbit)):
                    if(CssTable[ColumnInCss][LineInCss].nbit[NbItIndex] <=(2/len(HtmlPath))and CssTable[ColumnInCss][LineInCss].nbit[NbItIndex]>0):
                        tmp=""
                        tmp+= CssTable[ColumnInCss][LineInCss].name[NbItIndex]
                        Case[NOT_OFTENLY_FOUND][tmp] =  str(CssTable[ColumnInCss][LineInCss].nbit[NbItIndex])


    #fill the warning table

    for i in range(0,len(Case[NOT_FOUND])):
        WarningList[0].append(Case[NOT_FOUND][i])
    for i in range(0,len(Case[FUND_MULTIPLE_TIME])):
        WarningList[1].append(Case[FUND_MULTIPLE_TIME][i])

        WarningList[2]=Case[NOT_OFTENLY_FOUND]

pass
def AddToTable(Table, NameNewCssData, DataNewCssData):
    NewCssData = CssData("Undefined",NameNewCssData, ''.join(DataNewCssData), [0]*len(NameNewCssData))
    if(("#" in NameNewCssData)==True):
        NewCssData.type = Modifier3Name
        Table.append(NewCssData)
    elif(("." in NameNewCssData)==True):
        NewCssData.type = Modifier2Name
        Table.append(NewCssData)
    else:
        NewCssData.type = Modifier1Name
        Table.append(NewCssData)
pass
    ###############################
    ##END OF FUNCTION DECLARATION##
    ###############################
Window = Tk()

Window.resizable(width=False, height=False)
Window.title("Microchip CSS Optimizer "+ Version)
if(platform.system()=='Windows'):
    coef =1
    coefwindow=1
elif(platform.system()=='Darwin'):
    coef=0.72
    coefwindow=1.1
else:
    coef=0.6
    coefwindow=1.4

    ###############
    ##DEFINITIONS##
    ###############

#Definition for the Global WorkSpace

lfStep1 = tk.LabelFrame(Window, text="Step1:")
lfStep2 = tk.LabelFrame(Window, text="Step2:")
lfWarning = tk.LabelFrame(Window, text="Warning:")
lfStep3 = tk.LabelFrame(Window, text="Step3:")
Bottom = Label(Window, text="2016 - Developped by IoT & HASG Group - "+Version)
Bottom.grid(row=2, column=1)

#Definition for Step 1

TitleCss = tk.Label(lfStep1, text="Add a CSS file")
TextCss = StringVar()
entryCss = tk.Entry(lfStep1, textvariable=TextCss, width=int(42*coef), validate='key',validatecommand=EnableAddCss)
#entryCss.configure(highlightthickness=0)
BrowseCss = tk.Button(lfStep1, text="Browse", command=OpenCSS,width=int(10*coef))
#BrowseCss.configure(highlightthickness=0)
AddCss = tk.Button(lfStep1, text="Add CSS file", command=AddCSS, state="disable",width=int(15*coef))
#AddCss.configure(highlightthickness=0)

TitleHtml = tk.Label(lfStep1, text="Add an HTML file")
TextHtml = StringVar()
entryHtml = tk.Entry(lfStep1, textvariable=TextHtml, width=int(42*coef), validate='key',validatecommand=EnableAddCss)
BrowseHtml = tk.Button(lfStep1, text="Browse", command=OpenHTML,width=int(10*coef))
AddHtml = tk.Button(lfStep1, text="Add HTML file", command=AddHTML, state="disable",width=int(15*coef))
Read = tk.Button(lfStep1, text="Read CSS file", command=ReadFile,width=int(15*coef))

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

lfModifier = tk.LabelFrame(lfStep2)
TitleStep2 = Label(lfStep2, text="Select the desired definition to add to your CSS")
ModifierList = (Modifier1Name, Modifier2Name, Modifier3Name, Modifier4Name)
CBModifier = ttk.Combobox(lfStep2, values=ModifierList, state='readonly')
CBModifier.set(ModifierList[0])
CBModifier.bind('<<ComboboxSelected>>', RefreshStep2)
ChoiceList = ("None", "Default", "Current", "All")
CBSelChoice = ttk.Combobox(lfStep2, values=ChoiceList, state='readonly')
CBSelChoice.set(CBStep2State[4])
CBSelChoice.bind('<<ComboboxSelected>>', RefreshStep2)
ChoiceList2 = ("View All","Selected Only","Not Selected Only")
CBViewChoice = ttk.Combobox(lfStep2, values=ChoiceList2, state='readonly')
CBViewChoice.set(ChoiceList2[0])
CBViewChoice.bind('<<ComboboxSelected>>', RefreshStep2)
SearchBar = Entry(lfStep2, width=int(20*coef))
CallRefreshStep2 = lambda: RefreshStep2("")
BSearch = Button(lfStep2, text="Search", command=CallRefreshStep2)
#############################Id:3 definition########################################

ModifierWorkspace = tk.Frame(lfModifier)
ModifierWorkspace.grid_propagate(False)
ModifierWorkspace.grid(row=1, column=2, sticky="n s e w")
#############################Id:4 definition########################################

canvas = Canvas(ModifierWorkspace)
myscrollbar = Scrollbar(ModifierWorkspace, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
#############################Id:5 definition########################################

frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')
canvas.configure(width=1000, height=200)


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

frame4 = Frame(lfWarning)

#############################Id:3 definition########################################

ModifierWorkspaceWarning = tk.LabelFrame(frame4)
ModifierWorkspaceWarning.grid(row=1, column=2, sticky="n s e w")
TopBarPack = Frame(frame4)

#############################Id:4 definition########################################

CanvasWarning = Canvas(ModifierWorkspaceWarning)
myscrollbar2 = Scrollbar(ModifierWorkspaceWarning, orient="vertical", command=CanvasWarning.yview)
CanvasWarning.configure(yscrollcommand=myscrollbar2.set)

TopBarPack = Frame(frame4)
TitleTBP = tk.Label(TopBarPack, text="Hide Warnings: Name or PartName* are valid. Space required between elements")
TextSelector = StringVar()
TextSelector.set("!DOCTYPE head meta div script title html body")
EntrySelector = Entry(TopBarPack, textvariable=TextSelector, width=int(100*coef))
RefreshButton = Button(TopBarPack, text="Refresh", command=RefreshWarning)

#############################Id:5 definition########################################

frame2 = Frame(CanvasWarning)
CanvasWarning.create_window((0, 0), window=frame2, anchor='nw')
CanvasWarning.configure(width=1000, height=200)


#Definition for Step 3


Generate = tk.Button(lfStep3, text="Generate",command=IsClassic,width=int(15*coef))
GenerateDotMin = tk.Button(lfStep3, text="Generate .min",command=IsDotMin,width=int(15*coef))
Reset = tk.Button(lfStep3, text="Select new files",command=Reset,width=int(15*coef))



                                ######################
                                ##END OF DEFINITIONS##
                                ######################

RefreshStep1()

Window.mainloop()
