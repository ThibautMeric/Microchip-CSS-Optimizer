def Optimize(WarningList,HtmlTable,CssTable,HtmlPath):
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