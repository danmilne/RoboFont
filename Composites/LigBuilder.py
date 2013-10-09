"""
This script builds selected ligatures from components as defined in dictionary below.

"""

import random

f = CurrentFont()

LigDict = {

#Manually composed foreign
"AE" : ["A", "E"],
"AE.sc" : ["A.sc", "E.sc"],
"ae" : ["a", "e"],
"Aringacute" : ["A", "ring.cap", "acute.cap"],
"aringacute" : ["a", "ring", "acute"],
"Oslash" : ["O"],
"OE" : ["O", "E"],
"OE.sc" : ["O.sc", "E.sc"],
"germandbls" : ["f","s"],
"Eth" : ["D"],
"Thorn" : ["P"],
"Dcroat" : ["D"],
"Hbar" : ["H"],
"IJ" : ["I", "J"],
"IJ.sc" : ["I.sc", "J.sc"],
"IJacute" : ["Iacute", "Jacute"],
"Ldot" : ["L","L"],
"Lslash" : ["L"],
"Eng" : ["N"],
"Tbar" : ["T"],
"oslash" : ["o"],
"oe" : ["o", "e"],
"eth" : ["o", "parenright"],
"thorn" : ["p", "b"],
"dcroat" : ["d"],
"hbar" : ["h"],
"ij" : ["i", "j"],
"ijacute" : ["iacute", "jacute"],
"ldot" : ["l","l"],
"lslash" : ["l"],
"eng" : ["n"],
"tbar" : ["t"],
"germandbls.sc" : ["S.sc", "S.sc"],


#Standard unicode
"fi" : ["f","i"],
"fl" : ["f","l"],
"ff" : ["f","f"],
"ffi" : ["f","f","i"],
"ffl" : ["f","f","l"],

#Standard extended
"f_i" : ["f","i"],
"f_l" : ["f","l"],
"f_f" : ["f","f"],
"f_f_i" : ["f","f","i"],
"f_f_l" : ["f","f","l"],
"f_b" : ["f","b"],
"f_h" : ["f","h"],
"f_j" : ["f","j"],
"f_k" : ["f","k"],
"f_f_b" : ["f","f","b"],
"f_f_h" : ["f","f","h"],
"f_f_j" : ["f","f","j"],
"f_f_k" : ["f","f","k"],

#Misc
"T_h" : ["T","h"],
"t_t" : ["t","t"],
"t_y" : ["t","y"],
"t_t_y" : ["t","t","y"],
"f_t" : ["f","t"],
"s_t" : ["s","t"],
"c_t" : ["c","t"],
"g_f" : ["g", "f"],
"r_y" : ["r", "y"],
"DIONLEE" : ["D","I","O","N","space","L","E","E"],

#Standard Fractions:
'onehalf' : ['one.num','fraction','two.den'],
'onequarter' : ['one.num','fraction','four.den'],
'threequarters' : ['three.num','fraction','four.den'],
'onethird' : ['one.num','fraction','three.den'],
'twothirds' : ['two.num','fraction','three.den'],
'oneeighth' : ['one.num','fraction','eight.den'],
'threeeighths' : ['three.num','fraction','eight.den'],
'fiveeighths' : ['five.num','fraction','eight.den'],
'seveneighths' : ['seven.num','fraction','eight.den']


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

SelectedGlyphs = f.selection + f.templateSelection

## Build selected ligatures:

for lig in LigDict:
    if lig in SelectedGlyphs:
        BuildLig(lig)
        
        

        