def ConfigureCanvasStep2(event, lfStep2 ,WindowSetting):
    WidthCBModifier = 750*WindowSetting["Enlarge"]
    HeightCBModifier = 220*WindowSetting["Enlarge"]
    lfStep2.children["lfmodifier"].children["modifierworkspace"].children["canvas"].configure(scrollregion=lfStep2.children["lfmodifier"].children["modifierworkspace"].children["canvas"].bbox("all"), width=WidthCBModifier, height=HeightCBModifier)
pass
