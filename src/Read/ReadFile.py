from Optimizer.Optimize import *
from Read.ReadCss import *
from Read.ReadHtml import *
from Step1.RefreshStep1 import *
from Step2.RefreshStep2 import *
from Step3.RefreshStep3 import *
from StepWarning.RefreshWarning import *
import os

def ReadFile(Bottom, lfStep1, lfStep2, lfWarning, lfStep3, CssPath, HtmlPath, CssTable, HtmlTable, ModifierDict, WarningList, CBStep2State, ButtonList, ChoiceList, ChoiceList2, WindowSetting):

    #Unexpected action handler

    if(len(CssPath) == 0):
        try:
            tkinter.messagebox.showerror ("Error: No CSS", "Please add a CSS file")
        except:
            tkMessageBox.showerror ("Error: No CSS", "Please add a CSS file")
        return
    elif(len(HtmlPath) == 0):
        try:
            tkinter.messagebox.showerror ("Error: No HTML", "Please add an HTML file")
        except:
            tkMessageBox.showerror ("Error: No HTML", "Please add an HTML file")
        return
    else:

        Error = "The following files are unvalid:"
        DefaultErrorLenght = len(Error)
        RemoveCss = []
        RemoveHtml = []
        for i in range(0, len(CssPath)):
            if(os.path.isfile(str(CssPath[i])) == False):
                Error += "\n..." + CssPath[i][-40:] + ": Not Found" + "\n"
                RemoveCss.append(i)
        for i in RemoveCss[::-1]:
            CssPath.remove(CssPath[i])
        RemoveCss = []

        for i in range(0, len(HtmlPath)):
            if(os.path.isfile(str(HtmlPath[i])) == False):
                Error += "\n..." + HtmlPath[i][-40:] + ": Not Found" + "\n"
                RemoveHtml.append(i)
        for i in RemoveHtml[::-1]:
            HtmlPath.remove(HtmlPath[i])
        RemoveHtml = []

        for i in range(0, len(CssPath)):
            if(CssPath[i][-4] != "." or CssPath[i][-3] != "c" or CssPath[i][-2] != "s" or CssPath[i][-1] != "s"):
                Error += "\n..." + CssPath[i][-40:] + ": Not CSS" + "\n"
                RemoveCss.append(i)
        for i in RemoveCss[::-1]:
            CssPath.remove(CssPath[i])
        RemoveCss = []

        for i in range(0, len(HtmlPath)):
            if(HtmlPath[i][-5] != "." or HtmlPath[i][-4] != "h" or HtmlPath[i][-3] != "t" or HtmlPath[i][-2] != "m" or HtmlPath[i][-1] != "l"):
                Error += "\n..." + HtmlPath[i][-40:] + ": Not HTML" + "\n"
                RemoveHtml.append(i)
        for i in RemoveHtml[::-1]:
            HtmlPath.remove(HtmlPath[i])
        RemoveHtml = []

        for i in range(0, len(CssPath)):
            if(CssPath.count(CssPath[i]) > 1):
                Error += "\n..." + CssPath[i][-40:] + ": Found Multiple times" + "\n"
                RemoveCss.append(i)

        for i in RemoveCss[::-1]:
            del CssPath[i]
        RemoveCss = []

        for i in range(0, len(HtmlPath)):
            if(HtmlPath.count(HtmlPath[i]) > 1):
                Error += "\n..." + HtmlPath[i][-40:] + ": Found Multiple times" + "\n"
                RemoveHtml.append(i)

        for i in RemoveHtml[::-1]:
            del HtmlPath[i]
        RemoveHtml = []

        if(len(Error) > DefaultErrorLenght):
            try:
                tkinter.messagebox.showerror ("Error: Incorrect File(s)", Error)
            except:
                tkMessageBox.showerror ("Error: Incorrect File(s)", Error)
            RefreshStep1(lfStep1,WindowSetting, HtmlPath, CssPath)
            lfStep1.children["read"].grid(row=len(CssPath) + len(HtmlPath) + 9, column=0, pady="5")
            return


    # Disable path modifications

    lfStep1.children["browsecss"].configure(state="disabled")
    lfStep1.children["browsehtml"].configure(state="disabled")
    lfStep1.children["read"].configure(state="disabled")
    lfStep1.children["entryhtml"].configure(state="disabled")
    lfStep1.children["entrycss"].configure(state="disabled")

    #Read the files

    ReadCSS(CssPath, CssTable, ModifierDict)
    ReadHTML(HtmlPath, HtmlTable)
    Optimize(WarningList, HtmlTable, CssTable, HtmlPath)

    #Display Step 2

    RefreshStep2("", Bottom, lfStep2, CBStep2State, ModifierDict, CssTable, ButtonList, ChoiceList, ChoiceList2, WindowSetting)
    
    #Display warning

    RefreshWarning(lfWarning, WarningList, WindowSetting)

    #Display Step 3

    RefreshStep3(lfStep3)

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