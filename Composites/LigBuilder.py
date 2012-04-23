"""
This script builds selected ligatures from components as defined in dictionary below. Selected ligatures must already exist in font, so mark empty template glyphs with a colour before trying to build ligature.

"""

import random

f = CurrentFont()

LigDict = {

"ae" : ["a","e"],
"ij" : ["i","j"],
"oe" : ["o","e"],

"fi" : ["f","i"],
"fl" : ["f","l"],
"f_i" : ["f","i"],
"f_l" : ["f","l"],
"f_f" : ["f","f"],
"f_b" : ["f","b"],
"f_h" : ["f","h"],
"f_j" : ["f","j"],
"f_k" : ["f","k"],
"f_f_i" : ["f","f","i"],
"f_f_l" : ["f","f","l"],
"f_f_b" : ["f","f","b"],
"f_f_h" : ["f","f","h"],
"f_f_j" : ["f","f","j"],
"f_f_k" : ["f","f","k"],
"d_d_g" : ["d","d","g"],

"f.short" : ["f"],
"f_f.short" : ["f","f.short"]

}

###### MARK OPTIONS ###############

randombluegrey = (0.3,0.3,random.random(),0.8)

blue = (0,0,1,1)
green = (0,1,0,1)
yellow = (1,1,0,1)

markcolour = randombluegrey

###################################

def BuildLig(lig):
    f.newGlyph(lig)
    c_advance = 0
    advanceList = []
    for comp in LigDict[lig]:
        f[lig].appendComponent(comp,(c_advance,0))
        c_width = f[comp].width
        advanceList.append(c_width)
        c_advance = sum(advanceList)
    
    f[lig].width = c_advance
    f[lig].mark = markcolour
    f.update()


## Collect selected glyphs to avoid trying to build unwanted ligatures:

SelectedGlyphs = []

for g in f:
    if g.selected == True:
        SelectedGlyphs.append(g.name)

## Build selected ligatures:

for lig in LigDict:
    if lig in SelectedGlyphs:
        BuildLig(lig)
        
        

        