"""
This script is an extension of a script by Paul van der Laan.

It generates an InDesign Tagged Text file which compares glyphs from all open fonts.
A .txt file is generated in the working folder of the current font.
To use the .txt file, simply place it in an open InDesign document.

Glyphs are compared based on their order in the font (GID), so for this to work, fonts must have the same number of glyphs in the same order.

The script attempts to diagnose problems which relate to missing or extra glyphs.

Sorting all fonts with the same character set before generating them should help to match the orders.

"""

font = CurrentFont()

fontlen = len(font) + 1

## Generate Tagged Text page header:

headerlines = []

headerlines.append('<ASCII-MAC>')
headerlines.append('<vsn:7><fset:InDesign-Roman><ctable:=<Black:COLOR:CMYK:Process:0,0,0,1>>')
headerlines.append('<dps:NormalParagraphStyle=<Nextstyle:NormalParagraphStyle><ph:0>>')
headerlines.append('<pstyle:NormalParagraphStyle>')

## Generate lines for each glyph and append:

bodylines = []

for n in range(0, fontlen):
    glyphline = ''
    fontname = font.info.familyName
    stylename = font.info.styleName
    fontline = '<ct:' + str(stylename) + '><cf:' + str(fontname) + '><pSG:' + str(n) + '><0xFFFD><pSG:><ct:><cf:>'
    glyphline = glyphline + fontline
    
    bodylines.append(glyphline)

finalbodylines = ' '.join(bodylines)
headerlines.append(finalbodylines)

finallines = '\r'.join(headerlines)

## Create file path for txt file:

fontpath = font.path

pathparts = fontpath.split('/')
del pathparts[-1]

savepath = '/'.join(pathparts)


## Create file name from weight names of open fonts:

filenameparts = []

famname = font.info.familyName
nameparts = famname.split(' ') ## Remove spaces
newfamname = ''.join(nameparts)

stylename = font.info.styleName
styleparts = stylename.split(' ') ## Remove spaces
newstylename = ''.join(styleparts)

filenameparts.append(newfamname)
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

