f = CurrentFont()

"""
This script builds and rebuilds selected composite glyphs based on [base glyph, accent glyph and anchor] as defined in the accent list below.

"""

AccentList = [
	## LOWERCASE ########################################
	["agrave","a","grave","top"],
	["aacute","a","acute","top"],
	["acircumflex","a","circumflex","top"],
	["atilde","a","tilde","top"],
	["adieresis","a","dieresis","top"],
	["amacron","a","macron","top"],
	["abreve","a","breve","top"],
	["aring","a","ring","top"],
	# aringacute made manually
	["aeacute","ae","acute","top"],
	["cacute","c","acute","top"],
	["cacute.pl","c","acute.pl","top"],
	["ccircumflex","c","circumflex","top"],
	["ccaron","c","caron","top"],
	["cdotaccent","c","dotaccent","top"],
	["ccedilla","c","cedilla","bottom"],
	# dcaron made manually
	["egrave","e","grave","top"],
	["eacute","e","acute","top"],
	["ecircumflex","e","circumflex","top"],
	["ecaron","e","caron","top"],
	["edieresis","e","dieresis","top"],
	["emacron","e","macron","top"],
	["ebreve","e","breve","top"],
	["edotaccent","e","dotaccent","top"],
	["gcircumflex","g","circumflex","top"],
	["gcommaaccent","g","commaaccent.alt","top"],
	["gbreve","g","breve","top"],
	["gdotaccent","g","dotaccent","top"],
	["hcircumflex","h","circumflex","top"],
	["igrave","dotlessi","grave","top"],
	["iacute","dotlessi","acute","top"],
	["icircumflex","dotlessi","circumflex","top"],
	["itilde","dotlessi","tilde","top"],
	["idieresis","dotlessi","dieresis","top"],
	["ibreve","dotlessi","breve","top"],
	# imacron made manually
	# idotaccent made manually
	["jcircumflex","dotlessj","circumflex","top"],
	["kcommaaccent","k","commaaccent","bottom"],
	["lacute","l","acute","top"],
	["lcommaaccent","l","commaaccent","bottom"],
	# lcaron made manually
	# ldot made manually
	["nacute","n","acute","top"],
	["nacute.pl","n","acute.pl","top"],
	["ncaron","n","caron","top"],
	["ntilde","n","tilde","top"],
	["ncommaaccent","n","commaaccent","bottom"],
	["ograve","o","grave","top"],
	["oacute","o","acute","top"],
	["oacute.pl","o","acute.pl","top"],
	["ocircumflex","o","circumflex","top"],
	["otilde","o","tilde","top"],
	["odieresis","o","dieresis","top"],
	["omacron","o","macron","top"],
	["obreve","o","breve","top"],
	["ohungarumlaut","o","hungarumlaut","top"],
	["oslashacute","oslash","acute","top"],
	["racute","r","acute","top"],
	["rcaron","r","caron","top"],
	["rcommaaccent","r","commaaccent","bottom"],
	["sacute","s","acute","top"],
	["sacute.pl","s","acute.pl","top"],
	["scircumflex","s","circumflex","top"],
	["scaron","s","caron","top"],
	["scedilla","s","cedilla","bottom"],
	["scommaaccent","s","commaaccent","bottom"],
	# tcaron made manually
	["tcommaaccent","t","commaaccent","bottom"],
	["uni021B","t","commaaccent","bottom"],
	["ugrave","u","grave","top"],
	["uacute","u","acute","top"],
	["ucircumflex","u","circumflex","top"],                                                
	["utilde","u","tilde","top"],
	["udieresis","u","dieresis","top"],
	["umacron","u","macron","top"],
	["ubreve","u","breve","top"],
	["uring","u","ring","top"],
	["uhungarumlaut","u","hungarumlaut","top"],
	["wcircumflex","w","circumflex","top"],
	["wgrave","w","grave","top"],
	["wacute","w","acute","top"],
	["wdieresis","w","dieresis","top"],
	["ygrave","y","grave","top"],
	["yacute","y","acute","top"],
	["ycircumflex","y","circumflex","top"],
	["ydieresis","y","dieresis","top"],
	["zacute","z","acute","top"],
	["zacute.pl","z","acute.pl","top"],
	["zcaron","z","caron","top"],
	["zdotaccent","z","dotaccent","top"],
	
	## UPPERCASE ########################################
	["Agrave","A","grave","top"],
	["Aacute","A","acute","top"],
	["Acircumflex","A","circumflex","top"],
	["Atilde","A","tilde","top"],
	["Adieresis","A","dieresis","top"],
	["Amacron","A","macron","top"],
	["Abreve","A","breve","top"],
	["Aring","A","ring","top"],
	["Cacute","C","acute","top"],
	["Ccircumflex","C","circumflex","top"],
	["Ccaron","C","caron","top"],
	["Cdotaccent","C","dotaccent","top"],
	["Ccedilla","C","cedilla","bottom"],
	["Dcaron","D","caron","top"],
	["Egrave","E","grave","top"],
	["Eacute","E","acute","top"],
	["Ecircumflex","E","circumflex","top"],
	["Ecaron","E","caron","top"],
	["Edieresis","E","dieresis","top"],
	["Emacron","E","macron","top"],
	["Ebreve","E","breve","top"],
	["Edotaccent","E","dotaccent","top"],
	["Gcircumflex","G","circumflex","top"],
	["Gbreve","G","breve","top"],
	["Gdotaccent","G","dotaccent","top"],
	["Gcommaaccent","G","commaaccent","bottom"],
	["Hcircumflex","H","circumflex","top"],
	["Igrave","I","grave","top"],
	["Iacute","I","acute","top"],
	["Icircumflex","I","circumflex","top"],
	["Itilde","I","tilde","top"],
	["Idieresis","I","dieresis","top"],
	["Imacron","I","macron","top"],
	["Ibreve","I","breve","top"],
	["Idotaccent","I","dotaccent","top"],
	["Jcircumflex","J","circumflex","top"],
	["Kcommaaccent","K","commaaccent","bottom"],
	["Lacute","L","acute","top"],
	["Lcommaaccent","L","commaaccent","bottom"],
	["Nacute","N","acute","top"],
	["Ncaron","N","caron","top"],
	["Ntilde","N","tilde","top"],
	["Ncommaaccent","N","commaaccent","bottom"],
	["Ograve","O","grave","top"],
	["Oacute","O","acute","top"],
	["Ocircumflex","O","circumflex","top"],
	["Otilde","O","tilde","top"],
	["Odieresis","O","dieresis","top"],
	["Omacron","O","macron","top"],
	["Obreve","O","breve","top"],
	["Ohungarumlaut","O","hungarumlaut","top"],
	["Racute","R","acute","top"],
	["Rcaron","R","caron","top"],
	["Rcommaaccent","R","commaaccent","bottom"],
	["Sacute","S","acute","top"],
	["Scircumflex","S","circumflex","top"],
	["Scaron","S","caron","top"],
	["Scedilla","S","cedilla","bottom"],
	["Scommaaccent","S","commaaccent","bottom"],
	["Tcaron","T","caron","top"],
	["uni021A","T","commaaccent","bottom"],
	["Ugrave","U","grave","top"],
	["Uacute","U","acute","top"],
	["Ucircumflex","U","circumflex","top"],
	["Utilde","U","tilde","top"],
	["Udieresis","U","dieresis","top"],
	["Umacron","U","macron","top"],
	["Ubreve","U","breve","top"],
	["Uring","U","ring","top"],
	["Uhungarumlaut","U","hungarumlaut","top"],
	["Ygrave","Y","grave","top"],
	["Yacute","Y","acute","top"],
	["Ycircumflex","Y","circumflex","top"],
	["Ydieresis","Y","dieresis","top"],
	["Zacute","Z","acute","top"],
	["Zcaron","Z","caron","top"],
	["Zdotaccent","Z","dotaccent","top"]
]

print "--------------------------------"
if len(f.selection) == 0:
    print "Selection did not yield any composites. Select at least one existing glyph."
else:
    print "Building..."


def build_accents(accent_list):
    for glyph_name, base_comp, acc_comp, anchor in accent_list:
        if glyph_name in f and f[glyph_name].selected == True or base_comp in f and f[base_comp].selected == True or acc_comp in f and f[acc_comp].selected == True:
            if acc_comp in f:
                AnchorList = []
                for a in f[base_comp].anchors:
                    AnchorList.append(a.name)
                if anchor in AnchorList:
                    parts = [(acc_comp, anchor)]
                    result = f.compileGlyph(glyph_name, base_comp, parts)
                    print glyph_name
    f.update()


import datetime
now = datetime.datetime.now()
timestamp = now.strftime("%H-%M-%S")


build_accents(AccentList)
print "--------------------------------"
if len(f.selection) > 0:
    print"Accents built at " + str(timestamp)
