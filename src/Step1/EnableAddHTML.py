def EnableAddHtml(AddHtml,Text):
    if (Text!="Insert Path"):
        try:
            AddHtml.configure(state="active")
        except:
            AddHtml.configure(state="normal")
    if (len(Text)<2):
        AddHtml.configure(state="disable")
pass