"""
This script rounds points in the current glyph, auto-orders foreground contours, creates / clears the mask layer, copies the foreground layer to the mask layer and records the side-bearings in the glyph in g.lib.

Sidebearings can be replaced (using another script) after manipulating the contours.


"""
f = CurrentFont()
g = CurrentGlyph()


g.prepareUndo('copy contours to mask')

f.removeLayer("temp1")

# Round points in glyph to integers:

######################################

snap_value = 0.8

######################################

left_before = g.leftMargin
right_before = g.rightMargin

global_guides = []
for h in f.guides:
    global_guides.append(h.y)

key_y_values = f.info.postscriptBlueValues + \
                f.info.postscriptOtherBlues + \
                f.info.postscriptFamilyBlues + \
                f.info.postscriptFamilyOtherBlues + \
                global_guides

for c in g:
    for i in range(len(c.points)):

        if i == len(c.points) -1: 
            i_plus == 0
            i_minus = i - 1
            
        elif i == 0:
            i_plus = i + 1
            i_minus = len(c.points) -1
        else:
            i_plus = i + 1
            i_minus = i - 1
    
        if abs(c.points[i].x - c.points[i_minus].x) < 0.499 and abs(c.points[i].x - c.points[i_plus].x) < 0.499 :
            c.points[i].y = round(c.points[i].y)
            c.points[i].x = round(c.points[i].x)
        
        else: 
            for b in key_y_values:
                if abs(float(c.points[i].y) - b) < snap_value:
                    c.points[i].y = b
                    
            c.points[i].x = round(c.points[i].x)
            c.points[i].y = round(c.points[i].y)

g.leftMargin = round(left_before)
g.rightMargin = round(right_before)

g.update()

# AutoOrder foregound:

g.autoContourOrder()

for c in g:
    c.autoStartSegment()

# Copy to mask:

g.getLayer("mask", clear=True) #creates or clears and switches to mask layer
g.copyToLayer("mask", clear=True)


# Record sidebearings:

leftSB = str(g.name) + "_left"
rightSB = str(g.name) + "_right"

g.lib[leftSB] = g.leftMargin
g.lib[rightSB] = g.rightMargin

print "---------------------------------"
print "Sidebearings recorded in g.lib:"
print "---------------------------------"
print str(int(g.leftMargin)) + " | " + str(g.name) + " | " + str(int(g.rightMargin)) + "  // w = " + str(int(g.width))

g.performUndo()
g.update()
f.update()