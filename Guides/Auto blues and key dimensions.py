"""
This script calculates blue values and key dimensions based on existing glyphs in font.
Note that this script will change any existing values which you have set manually.

Any blue values which cannot be determined from existing glyphs take the value calaculated for the baseline overshoot.
If the baseline overshoot cannot be determined, a default value is used (defined on line 87).

"""

f = CurrentFont()


## Find the extreme points in a glyph (min or max):

def ExtremeGlyph(top_bottom, glyph):
    y_list = []
    g = f[glyph]
    
    for c in g:
        for p in c.points:
            y_list.append(p.y)
    if top_bottom == 'bottom':
        return min(y_list)
    if top_bottom == 'top':
        return max(y_list)
  
    
## Check if in font then find extremes:

def ExtremePoint(min_max, top_bottom, List):
    InFont = []
    for glif in List:
        if glif in f and len(f[glif]) > 0:
            InFont.append(glif)
    X_Vals = []

    if len(InFont) > 0:

        if min_max == 'Min':
            for h in InFont:
                i = ExtremeGlyph(top_bottom, h)
                X_Vals.append(i)
            x = int(min(X_Vals))
            BluePair['min'] = x

        if min_max == 'Max':
            for h in InFont:
                i = ExtremeGlyph(top_bottom, h)
                X_Vals.append(i)
            x = int(max(X_Vals))
            BluePair['max'] = x


## Check pair for missing values, estimate them and add pair to Blue List:

def AddPair(pair_list):
    if len(BluePair) < 1:
        print 'Unable to determine blue values for ' + Name

    else:    
        if 'min' not in BluePair:
            print 'Estimating value for ' + Name + '_min'
            BluePair['min'] = BluePair['max'] - overshoot

        if 'max' not in BluePair:
            print 'Estimating value for ' + Name + '_max'
            BluePair['max'] = BluePair['min'] + overshoot
    
        pair_list.append(BluePair['min'])
        pair_list.append(BluePair['max'])
        
        BlueSize = abs(BluePair['max'] - BluePair['min'])
        ZoneSizes.append(BlueSize)
        print 'Overshoot at ' + Name + ' is ' + str(BlueSize)

################################################
## If possible, determine value for default overshoot:

BluePair = {}
B_Base_min = ['C','G','O','S','c','e','o','s']
ExtremePoint('Min', 'bottom', B_Base_min)

if len(BluePair) > 0:
    overshoot = abs(int(BluePair['min']))
    print '================================================================='
    print 'Default value for overshoot (=' + str(overshoot) + ') determined by existing glyphs'
    print '================================================================='
else:
    overshoot = 10
    print '================================================================='
    print 'Default value for overshoot (=' + str(overshoot) + ') determined by manual value (line 79)'
    print '================================================================='
                

################################################
BlueVals = []
OtherBlueVals = []
ZoneSizes = []

################################################
## Determine pair of blue values for Descenders:

BluePair = {}

Name = 'Descenders'

B_Desc_min = ['g','j','y']
ExtremePoint('Min', 'bottom', B_Desc_min)

B_Desc_max = ['p','q']
ExtremePoint('Max', 'bottom', B_Desc_max)

AddPair(OtherBlueVals)


################################################
## Determine pair of blue values for Baseline:

BluePair = {}

Name = 'Baseline'

B_Base_min = ['C','G','O','S','c','e','o','s']
ExtremePoint('Min', 'bottom', B_Base_min)

BluePair['max'] = 0

AddPair(BlueVals)


################################################
## Determine pair of blue values for x-height:

BluePair = {}

Name = 'x-height'

B_x_min = ['v','w','x','y','z']
ExtremePoint('Min', 'top', B_x_min)

B_x_max = ['a','c','e','n','o','s']
ExtremePoint('Max', 'top', B_x_max)

AddPair(BlueVals)

if 'min' in BluePair:
    xh = BluePair['min']
else:
    xh = 0

################################################
## Determine pair of blue values for Cap-height:

BluePair = {}

Name = 'Cap-height'

B_Cap_min = ['E','F','H','I','J','K','L','T','U','V','X','Y','Z']
ExtremePoint('Min', 'top', B_Cap_min)

B_Cap_max = ['A','C','G','M','O','Q','S']
ExtremePoint('Max', 'top', B_Cap_max)

AddPair(BlueVals)

if 'min' in BluePair:
    Caph = BluePair['min']
else:
    Caph = 0
    
################################################
## Determine pair of blue values for Ascenders:

BluePair = {}

Name = 'Ascenders'

B_Asc_min = ['b','d','h','k','l']
ExtremePoint('Min', 'top', B_Asc_min)

B_Asc_max = ['f']
ExtremePoint('Max', 'top', B_Asc_max)

AddPair(BlueVals)

## Deal with potential zero value:

if BlueVals[-1] - BlueVals[-2] < 1:
    BlueVals[-2] = BlueVals[-1] - overshoot
    print '================================================================='
    print 'Check Ascender overshoot. Zero value adjusted to default.'
    print '================================================================='


################################################
## Set Blue Values in font:
f.prepareUndo('Set Blue Values')
f.info.postscriptBlueValues = BlueVals
f.info.postscriptOtherBlues = OtherBlueVals
print '================================================================='
print 'Blue Values set in font: ' + str(BlueVals)
print 'Other Blue Values set in font: ' + str(OtherBlueVals)
print '================================================================='

f.info.postscriptBlueFuzz = 0 # Recommended value
print 'Set BlueFuzz value to 0 (recommended value)'

#f.info.postscriptBlueShift = 7
print 'BlueShift left as default value'

## Calculate BlueScale:
MaxZoneSize = max(ZoneSizes)
f.info.postscriptBlueScale = 3/float(4 * MaxZoneSize)

print 'Calculated BlueScale value: ' + str(f.info.postscriptBlueScale)
print '================================================================='

################################################
## Set Key Dimensions in font:

print 'KEY DIMENSIONS:'

if xh > 0:
    f.info.xHeight = xh
    print 'x-height set to ' + str(xh)

if Caph > 0:
    f.info.capHeight = Caph
    print 'Cap-height set to ' + str(Caph)

## Determine Asc/Desc values and round to nearest 10:
if f.info.unitsPerEm == 1000:
    if len(OtherBlueVals) > 0:
        Gap = float(1000 - (BlueVals[-1] - OtherBlueVals[0]))/10
        if Gap > 0:
            Asch = 10 * int((round((BlueVals[-1]/10)+(Gap/2))))
            Desch = Asch - 1000
            f.info.ascender = Asch
            print 'Ascender set to ' + str(Asch)
            f.info.descender = Desch
            print 'Descender set to ' + str(Desch)
            print '================================================================='

        else:
            print '================================================================='
            print 'Ascender and Descender exceed 1000 units. Check dimensions.'
            print '================================================================='
    else:
        print '================================================================='
        print 'Unable to calculate key Descender value.\nSetting based on Ascender or Cap-height value.'
        print '================================================================='
        Gap = 1000 - BlueVals[-1]
        f.info.ascender = BlueVals[-1] + (Gap/2)
        f.info.descender = f.info.ascender - 1000 
else:
    print '================================================================='
    print 'Font is not 1000 units per Em.\nPlease calculate Ascender and Descender values manually.'
    print '================================================================='


f.performUndo()

f.update()