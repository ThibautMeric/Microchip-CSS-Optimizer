def EnableAddCss(AddCss,Text):
    if (Text!="Insert Path"):
        try:
            AddCss.configure(state="active")
        except:
            AddCss.configure(state="normal")
    if (len(Text)<2):
        AddCss.configure(state="disable")
pass