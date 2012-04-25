"""
Replaces sidebearings of current glyph with those recorded earlier in g.lib (using the Copy to Mask script).

"""
g = CurrentGlyph()

left_before = g.leftMargin
right_before = g.rightMargin

leftSB = str(g.name) + "_left"
rightSB = str(g.name) + "_right"

def metrics():
    print str(int(g.leftMargin)) + " | " + str(g.name) + " | " + str(int(g.rightMargin)) + "  // w = " + str(int(g.width))

print "---------------------------------"
metrics()
print "---------------------------------"

if leftSB in g.lib:
    if g.lib[leftSB] == left_before and g.lib[rightSB] == right_before:
        print "Sidebearings have not changed."
    
    else:
        print "Sidebearings reverted:"
        g.leftMargin = g.lib[leftSB]
        g.rightMargin = g.lib[rightSB]
        metrics()

    
else:
    print "No sidebearings exist in g.lib"


