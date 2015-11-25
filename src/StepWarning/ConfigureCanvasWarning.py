def ConfigureCanvasWarning(event,lfWarning ,WindowSetting):
    WidthWarning = 1200*WindowSetting["Enlarge"]
    HeightWarning = 300*WindowSetting["Enlarge"]
    lfWarning.children["frame4"].children["modifierworkspacewarning"].children["canvaswarning"].configure(scrollregion=lfWarning.children["frame4"].children["modifierworkspacewarning"].children["canvaswarning"].bbox("all"), width=WidthWarning, height=HeightWarning)
pass