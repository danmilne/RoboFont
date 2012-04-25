"""
This slider controls interpolation between foreground and mask layers.
Initial position for slider is at 1.0 (current foreground outline)
Sliding left to 0.0 interpolates to mask
Sliding right to 3.0 extrapolates away from mask.

NOTE: 
Running this script opens an observer on the current glyph in the Glyph View window.
The slider window must then be closed before it can be used on another glyph.

"""


from fontTools.misc.transform import Transform
from vanilla import *

g = CurrentGlyph()


g.prepareUndo('interpolate with mask')


################### PREPOLATION ###################################

## Auto contour order and startpoints for foreground:

#g.autoContourOrder()

#for c in g:
#    c.autoStartSegment()

## Auto contour order and startpoints for mask:

g.flipLayers("foreground", "mask")

#g.autoContourOrder()

#for c in g:
#    c.autoStartSegment()

## Gather point info for mask layer:

maskpoints = []

for i in range(len(g)):
    maskpoints.append([])
    for j in range(len(g[i])):
        maskpoints[i].append((g[i][j].onCurve.x,g[i][j].onCurve.y))

## Gather point info for foreground layer:

g.flipLayers("mask", "foreground")

forepoints = []

for i in range(len(g)):
    forepoints.append([])
    for j in range(len(g[i])):
        forepoints[i].append((g[i][j].onCurve.x,g[i][j].onCurve.y))
        
## Compare length of each contour in mask and foreground:

n = 0

print '-------------------------------'
print 'Checking ' + str(g.name) + ' without auto ordering'

def gradient(point1, point2):
    grad = (point2[1] - point1[1])/(point2[0] - point1[0] + 0.9)
    return grad

mismatched = []
    
if len(maskpoints) == len(forepoints):
    for i in range(len(forepoints)):
        print '-------------------------------'
        if len(forepoints[i]) == len(maskpoints[i]):
            print 'Contour ' + str(i) + ' matches'
        else:
            n = n + 1
            print 'Contour ' + str(i) + ':'
            print str(len(forepoints[i])) + ' points in foreground'
            print str(len(maskpoints[i])) + ' points in mask'
            print '-------------------------------'
            
            if len(forepoints[i]) > len(maskpoints[i]):
                count = len(maskpoints[i])
                prob = 'mask'
            else:
                count = len(forepoints[i])
                prob = 'foreground'
            
            for j in range(-1,count - 1):
                def foregradient(a,b):
                    foregrad = gradient(forepoints[a][b],forepoints[a][b+1])
                    return foregrad
                
                def maskgradient(a,b):
                    maskgrad = gradient(maskpoints[a][b],maskpoints[a][b+1])
                    return maskgrad
                
                foregrad = foregradient(i,j)
                maskgrad = maskgradient(i,j)
                    
                if foregrad > 20:
                    foregrad = 100
                if maskgrad > 20:
                    maskgrad = 100
                if foregrad < -20:
                    foregrad = -100
                if maskgrad < -20:
                    maskgrad = -100
                  
                if abs(foregrad - maskgrad) > 0.4:
                    mismatched.append(j+1)
                    mismatched = [mismatched[0]]
                
                    ## Find second problem:
                
                    if prob == 'foreground':
                        foregrad = foregradient(i,j)
                        maskgrad = maskgradient(i,j+1)
                    else:
                        foregrad = foregradient(i,j+1)
                        maskgrad = maskgradient(i,j)
                    
                    if foregrad > 20:
                        foregrad = 100
                    if maskgrad > 20:
                        maskgrad = 100
                    if foregrad < -20:
                        foregrad = -100
                    if maskgrad < -20:
                        maskgrad = -100
                
                    if abs(foregrad - maskgrad) > 0.4:
                        mismatched.append(j+1)
                   
                
                
            if abs(len(forepoints[i]) - len(maskpoints[i])) == 1:
                if len(mismatched) == 1:
                    print 'Check between points ' + str(mismatched[0]) + ' and ' + str(mismatched[0] + 1)
                else:
                    print 'Check amongst the last few points'
            else:
                if len(mismatched) == 2:
                    print 'Check between points ' + str(mismatched[0]) + ' and ' + str(mismatched[0] + 1)
                    print 'Check between points ' + str(mismatched[1]) + ' and ' + str(mismatched[1] + 1)
                elif len(mismatched) == 1:
                    print 'Check between points ' + str(mismatched[0]) + ' and ' + str(mismatched[0] + 1)
                    print 'Check amongst the last few points'
                else:
                    print 'Check amongst the last few points'

else:
    print '-------------------------------'
    print 'Foreground has ' + str(len(forepoints)) + ' contours'
    print 'Mask has ' + str(len(maskpoints)) + ' contours'

print '-------------------------------'

################### INTERP SLIDER ###################################

 
## Collect mask points:

g.flipLayers("foreground", "mask")

all_mask_points = []
all_mask_points_length = []

for i in range(len(g)):
    all_mask_points.append([])
    for j in range(len(g[i].points)):
        all_mask_points[i].append((g[i].points[j].x, g[i].points[j].y))
        all_mask_points_length.append(j)

## Collect initial foreground points:
    
g.flipLayers("mask", "foreground")

all_fore_points = []
all_fore_points_length = []

for i in range(len(g)):
    all_fore_points.append([])
    for j in range(len(g[i].points)):
        all_fore_points[i].append((g[i].points[j].x, g[i].points[j].y))
        all_fore_points_length.append(j)

## Check for compatibility:
    
if n > 0:
    pass

else:

## if compatible, interpolate:

    def interp_fore(Glif, int_val):
        for i in range(len(Glif)):
            for j in range(len(Glif[i].points)):
                fore_point = all_fore_points[i][j]
                mask_point = all_mask_points[i][j]
                Glif[i].points[j].x = mask_point[0] + ((fore_point[0] - mask_point[0]) * int_val)
                Glif[i].points[j].y = mask_point[1] + ((fore_point[1] - mask_point[1]) * int_val)

    class InterpWithMaskWindow:
        def __init__(self, glyph):
            if glyph is None:
                print "There should be a glyph window selected."
                return
            self.glyph = glyph

            self.w = Window((600, 36),"Interpolate Foreground with Mask (no AutoOrder):")

            self.w.int = Slider((10, 6, -10, 22), value=1,
                                            maxValue=3,
                                            minValue=0,
                                            callback=self.adjust)

            self.w.open()

        def adjust(self, sender):
            int_val = self.w.int.get()
            print round(int_val, 2)
 
            Glif = self.glyph
        
            interp_fore(Glif, int_val)
        
            Glif.update()

    OpenWindow(InterpWithMaskWindow, CurrentGlyph())
           
g.update()
g.performUndo()

t = Transform().translate(0, 0)
g.transform(t, doComponents=True)
g.update()

