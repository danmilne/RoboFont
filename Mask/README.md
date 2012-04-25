MASK
==========
Assorted Python scripts for working with the mask layer. See scripts for more details.

Copy to Mask
-------------
This script rounds points in the current glyph, auto-orders foreground contours, creates / clears the mask layer, copies the foreground layer to the mask layer and records the side-bearings in the glyph in g.lib.

Recorded sidebearings can be replaced (using another script) after manipulating the contours.

Interpolate Slider scripts
-------------------------
This slider controls interpolation between foreground and mask layers (see more detailed documentation in scripts).

Before intrpolation, this script prepolates outlines in foreground and mask layers and attempts to diagnose any problems. If prepolation fails for matching outlines, try the Alt Interpolation slider, which uses another algorithm for selecting contour order and startpoints. If this also fails, you can order contours manually and use the slider without prepolation.

Replace Recorded Sidebearings
-------------------------
Replaces sidebearings of current glyph with those recorded earlier in g.lib (using the Copy to Mask script).