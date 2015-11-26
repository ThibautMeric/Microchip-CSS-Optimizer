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

def FillCanvasWarning(lfWarning,WarningList):
    DisplayWarning1 = []
    DisplayWarning2 = []
    DisplayWarning3 = []
    Display = [DisplayWarning1,DisplayWarning2,DisplayWarning3]
    tmp=[]
    HideContainingX = []
    HideNamedX = []
    Displaymodifier = [HideContainingX,HideNamedX]
    tmp2 = ""
    tmp2 = ''.join(map(str,lfWarning.children["frame4"].children["topbarpack"].children["entryselector"].get()))

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

    for widget in lfWarning.children["frame4"].children["modifierworkspacewarning"].children["canvaswarning"].children["frame2"].winfo_children():
        widget.destroy()

    #Display the number of errors

    lfWarning.children["frame4"].children["modifierworkspacewarning"].configure(text=str(len(Display[0])+len(Display[1])+len(Display[2])) + " warning(s):")

    #label = tk.Label(frame2, text=str(len(Display[0])+len(Display[1])+len(Display[2])) + " warning(s):", fg="red")
    #label.grid(row=1, column=0, sticky="w")

    #Display the Warnings

    Column = 1
    Row = 1
    MaxColumn=2

    for index in range (0,len(Display)):
        Column = 1
        for i in range(1,len(Display[index])+1):

            label = tk.Label(lfWarning.children["frame4"].children["modifierworkspacewarning"].children["canvaswarning"].children["frame2"], text=Display[index][i-1], fg="red")
            label.grid(row=Row, column=Column, sticky="w",padx=5, pady=5)
            Column+=1
            if (Column>MaxColumn):
               Column = 1
               Row +=1
        if(index+1<len(Display)):
            if (len(Display[index+1])>0):
                Row +=1
                label = tk.Label(lfWarning.children["frame4"].children["modifierworkspacewarning"].children["canvaswarning"].children["frame2"], text="----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------", fg="red")
                label.grid(row=Row, column=1,columnspan=2, pady=5, sticky="w")
                Row +=1


pass
