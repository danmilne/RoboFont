"""
Generates all combinations of the selected glyphs and sends them to the current space center window

"""

from mojo.UI import *

f = CurrentFont()

list = f.selection
combined_list = []

for a in list:
	for b in list:
		combined_list.append(a)
		combined_list.append(b)

SC = CurrentSpaceCenter()
if SC is not None:
    CurrentSpaceCenter().set(combined_list)
else:
    print "There is no space center window open."