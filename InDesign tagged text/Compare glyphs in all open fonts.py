"""
This script is an extension of a script by Paul van der Laan.

It generates an InDesign Tagged Text file which compares glyphs from all open fonts.
A .txt file is generated in the working folder of the current font.
To use the .txt file, simply place it in an open InDesign document.

A list of all glyphs in all open fonts is created. The script then runs through each glyph in the list, checking if it exists in each font and writing tagged text code which includes Font name, style and glyph GID number.

"""

allopen = AllFonts()

## Reorder open fonts according to family, width, weight (in that order):

unordered = []
for i in range(len(allopen)):
    family = allopen[i].info.familyName
    if allopen[i].info.italicAngle is not None:
        slope = abs(allopen[i].info.italicAngle)
    else:
        slope = 0
        
    weight = allopen[i].info.openTypeOS2WeightClass
    if weight == None:
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        print 'OpenType weight class is not defined in ' + str(family) + '. Order may be incorrect.'
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'

    width = allopen[i].info.openTypeOS2WidthClass
    if width == None:
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
        print 'OpenType width class is not defined in ' + str(family) + '. Order may be incorrect.'
        print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
            
    unordered.append((i,family,slope,width,weight))

ordered_weight = sorted(unordered, key=lambda tup: tup[4]) # reverse sort on weight
ordered_width = sorted(ordered_weight, key=lambda tup: tup[3]) # reverse sort on width
ordered_slope = sorted(ordered_width, key=lambda tup: tup[2]) # reverse sort on slope
ordered_family = sorted(ordered_slope, key=lambda tup: tup[1]) # reverse sort on family


ordered_open = []
for item in ordered_family:
    ordered_open.append(allopen[item[0]])
    
## Create a list of all glyphnames in all open fonts:

lenfonts = []

for font in ordered_open:
    fontlength = len(font)
    lenfonts.append((fontlength,font))
 
length_sort = sorted(lenfonts, key=lambda tup: tup[0], reverse = True) # reverse sort on length

glyphname_list = []
for PAIR in length_sort:
    FONT = PAIR[1]
    for glyphname in FONT.glyphOrder:
        if glyphname not in glyphname_list:
            glyphname_list.append(glyphname)


## Generate Tagged Text page header:

headerlines = []

headerlines.append('<ASCII-MAC>')
headerlines.append('<vsn:7><fset:InDesign-Roman><ctable:=<Black:COLOR:CMYK:Process:0,0,0,1>>')
headerlines.append('<dps:NormalParagraphStyle=<Nextstyle:NormalParagraphStyle><ph:0>>')
headerlines.append('<pstyle:NormalParagraphStyle>')

## Generate lines for each glyph and append:

bodylines = []


for GLYPHNAME in glyphname_list:
    glyphline = ''
    for font in ordered_open:
        if GLYPHNAME in font.glyphOrder:
            fontname = font.info.familyName
            stylename = font.info.styleName
            GID = font.glyphOrder.index(GLYPHNAME)
            fontline = '<ct:' + str(stylename) + '><cf:' + str(fontname) + '><pSG:' + str(GID) + '><0xFFFD><pSG:><ct:><cf:>'
            glyphline = glyphline + fontline
    
    bodylines.append(glyphline)

finalbodylines = ' '.join(bodylines)
headerlines.append(finalbodylines)

finallines = '\r'.join(headerlines)

## Create file path for txt file:

f = CurrentFont()
fontpath = f.path

pathparts = fontpath.split('/')
del pathparts[-1]

savepath = '/'.join(pathparts)


## Create file name from weight names of open fonts:

filenameparts = []

famname = f.info.familyName
nameparts = famname.split(' ') ## Remove spaces
newfamname = ''.join(nameparts)
filenameparts.append(newfamname)

## Add a timestamp:

import datetime
now = datetime.datetime.now()
timestamp = now.strftime("%m-%d_%H-%M")
filenameparts.append(timestamp)

filenameparts.append("weight")

for font in ordered_open:
    stylename = font.info.styleName
    stylenameparts = stylename.split(' ') ## Remove spaces
    newstylename = ''.join(stylenameparts)
    filenameparts.append(newstylename)


filename = '_'.join(filenameparts)
filename = str(savepath) + '/' + str(filename)+'.txt'


## Write txt file:

try:
    f = open(filename, "w")
    try:    
        f.writelines(finallines) # Write a sequence of strings to a file
    finally:
        f.close()
except IOError:
    pass

print '-------------------------------------'
print 'Generated Adobe tagged text file:'
print filename
print '-------------------------------------'