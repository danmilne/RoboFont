"""
Generates the current font hinted to the InDesign Fonts folder.

Path to InDesign folder may need to be updated depending on version.

"""

f = CurrentFont()

OTF_name = f.info.familyName + "-" + f.info.styleName + ".otf"

INDD_path = "/Applications/Adobe InDesign CS5/Fonts/"

otf_path = str(INDD_path) + str(OTF_name)

print "==================================================="
print "Generating " + str(OTF_name) + "..."
f.generate(otf_path, "otf", decompose=True, checkOutlines=True, autohint=True, releaseMode=False, glyphOrder=None)
print "Generated " + str(OTF_name)
print "To folder: " + str(INDD_path)
print "==================================================="