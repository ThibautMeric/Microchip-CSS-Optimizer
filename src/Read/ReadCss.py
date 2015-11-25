from Others.AddToTable import*

def ReadCSS(CssPath,CssTable,ModifierDict):

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

                NewAtRule = AtRuleData(ModifierDict["Modifier4"], [''.join(NameNewCssData)], "", [0])

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

                    if(( "@" in str(NameTable)) == True):AddToTable(NewAtRule.ModifierTable[3], NameTable, DataNewCssDataForAtRule, ModifierDict)
                    elif(( "#" in str(NameTable)) == True):AddToTable(NewAtRule.ModifierTable[2], NameTable, DataNewCssDataForAtRule, ModifierDict)
                    elif(( "." in str(NameTable)) == True):AddToTable(NewAtRule.ModifierTable[1], NameTable, DataNewCssDataForAtRule, ModifierDict)
                    else:AddToTable(NewAtRule.ModifierTable[0], NameTable, DataNewCssDataForAtRule, ModifierDict)

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
                        AddToTable(CssTable[2], NameTable, DataNewCssData, ModifierDict)
                    elif(( "." in NameTable[0]) == True):
                        AddToTable(CssTable[1], NameTable, DataNewCssData, ModifierDict)
                    else:
                        AddToTable(CssTable[0], NameTable, DataNewCssData, ModifierDict)

pass