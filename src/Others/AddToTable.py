try:
    from tkinter import *
except:
    from Tkinter import *

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

def AddToTable(Table, NameNewCssData, DataNewCssData,ModifierDict):
    NewCssData = CssData("Undefined",NameNewCssData, ''.join(DataNewCssData), [0]*len(NameNewCssData))
    if(("#" in NameNewCssData)==True):
        NewCssData.type = ModifierDict["Modifier3"]
        Table.append(NewCssData)
    elif(("." in NameNewCssData)==True):
        NewCssData.type = ModifierDict["Modifier2"]
        Table.append(NewCssData)
    else:
        NewCssData.type = ModifierDict["Modifier1"]
        Table.append(NewCssData)
pass