"""
This script is an extension of a script by Paul van der Laan.

It generates an InDesign Tagged Text file which compares glyphs from all open fonts.
A .txt file is generated in the working folder of the current font.
To use the .txt file, simply place it in an open InDesign document.

Glyphs are compared based on their order in the font (GID), so for this to work, fonts must have the same number of glyphs in the same order.

The script attempts to diagnose problems which relate to missing or extra glyphs.

Sorting all fonts with the same character set before generating them should help to match the orders.

"""

allopen = AllFonts()

## Reorder open fonts according to family, width, weight (in that order):

unordered = []
for i in range(len(allopen)):
    family = allopen[i].info.familyName
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
            
    unordered.append((i,family,width,weight))

ordered_weight = sorted(unordered, key=lambda tup: tup[3]) # reverse sort on weight
ordered_width = sorted(ordered_weight, key=lambda tup: tup[2]) # reverse sort on width
ordered_family = sorted(ordered_width, key=lambda tup: tup[1]) # reverse sort on weight


ordered_open = []
for item in ordered_family:
    ordered_open.append(allopen[item[0]])
    

## Determine number of glyphs in largest style:

lenfonts = []

for font in ordered_open:
    lenfonts.append(len(font))
    
lenlongest = max(lenfonts)


## Generate Tagged Text page header:

alllines = []

alllines.append('<ASCII-MAC>')
alllines.append('<vsn:7><fset:InDesign-Roman><ctable:=<\_spot\_Black:COLOR:CMYK:Process:0,0,0,1>>')
alllines.append('<dps:NormalParagraphStyle=<Nextstyle:NormalParagraphStyle><cc:\_spot\_Black><cs:10.000000><pmcbh:3><pmcah:3><phc:0><pswh:6><cf:Warnock Pro><cfs:Proportional Oldstyle><pkl:1><prao:10.000000><phlw:0><pswa:Left><phcf:0>>')
alllines.append('<pstyle:NormalParagraphStyle>')

## Generate lines for each glyph and append:

for n in range(0, lenlongest):
    glyphline = ''
    for font in ordered_open:
        fontname = font.info.familyName
        stylename = font.info.styleName
        fontline = '<ct:' + str(stylename) + '><cf:' + str(fontname) + '><pSG:' + str(n) + '><0xFFFD><pSG:><ct:><cf:>'
        glyphline = glyphline + fontline
    
    alllines.append(glyphline)

finallines = '\r'.join(alllines)

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

for font in ordered_open:
    stylename = font.info.styleName
    stylenameparts = stylename.split(' ') ## Remove spaces
    newstylename = ''.join(stylenameparts)
    filenameparts.append(newstylename)

## Add a timestamp:

import datetime
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M")
filenameparts.append(timestamp)

filename = '_'.join(filenameparts)
filename = str(savepath) + '/' + str(filename)+'.txt'


## Write txt file:

try:
    f = open(filename, "w")
    #f.write('blah') # Write a string to a file
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
print

## Determine missing glyphs in all open fonts

allglyphnames = {}

for font in ordered_open:
    for glyph in font:
        if glyph.name not in allglyphnames:
            allglyphnames[glyph.name] = 1
        else:
            allglyphnames[glyph.name] = allglyphnames[glyph.name] + 1

probglyphs = []
for n in allglyphnames:
    key = str(n)
    if allglyphnames[key] < len(ordered_open):
        probglyphs.append(n)
        
for glyph in probglyphs:
    missingfonts = []
    for font in ordered_open:
        if glyph not in font:
            missingfonts.append(font)
    string = ''
    for f in missingfonts:
        string = string + f.info.familyName + " - " + str(f.info.styleName) + ', '
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
    print str(glyph) + ' is missing from ' + string
    print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'

