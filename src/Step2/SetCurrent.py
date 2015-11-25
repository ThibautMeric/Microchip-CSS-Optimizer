def SetCurrent():
    CBSelChoice.set(ChoiceList[2])
    CBStep2State[ModifierList.index(CBModifier.get())]=CBSelChoice.get()
pass