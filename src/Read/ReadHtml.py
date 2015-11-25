

def ReadHTML(HtmlPath, HtmlTable):
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