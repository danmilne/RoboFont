"""
A tweaked version of Frederik Berlaen's Multi-Font Preview script.

This version orders the open fonts according to family, slope, width, weight (in that order).

OpenType weight and width classes must be set in the font info for this to work!

"""

import vanilla
from defconAppKit.windows.baseWindow import BaseWindowController
from defconAppKit.controls.glyphLineView import GlyphLineView
from mojo import events

allopen = AllFonts()

## Reorder open fonts according to family, width, weight:

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
ordered_family = sorted(ordered_slope, key=lambda tup: tup[1]) # reverse sort on weight


ordered_open = []
for item in ordered_family:
    ordered_open.append(allopen[item[0]])
    
    

class MultiFontPreview(BaseWindowController):

    def __init__(self):
        self.w = vanilla.Window((400, 400), minSize=(100, 100))
        self.w.glyphLineView = GlyphLineView((0, 0, 0, 0), pointSize=None, autohideScrollers=False, showPointSizePlacard=True)
        events.addObserver(self, "glyphChanged", "currentGlyphChanged")
        self.glyphChanged(dict(glyph=CurrentGlyph()))
        self.setUpBaseWindowBehavior()
        self.w.open()

    def windowCloseCallback(self, sender):
        events.removeObserver(self, "currentGlyphChanged")
        super(MultiFontPreview, self).windowCloseCallback(sender)

    def glyphChanged(self, info):
        # RoboFont v1.2:
        # glyph = info["glyph"]
        # RoboFont v1.3+:
        glyph = CurrentGlyph()
        if glyph is None:
            glyphs = []
        else:
            glyphName = glyph.name
            glyphs = [font[glyphName].naked() for font in ordered_open if glyphName in font]
        self.w.glyphLineView.set(glyphs)

MultiFontPreview()