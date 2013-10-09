"""
This script builds and rebuilds selected composite glyphs based on [base glyph, accent glyph and anchor] as defined in the accent dictionary below.

The script confirms that both base glyph and accent glyph exist and have the necessary anchors before proceeding.

It also checks if the resulting composite glyph exists in the template and whether existing composite glyphs contain any contours before rebuilding them. (This avoids losing decomposed / modified accent glyphs).

Use alternative script "Build sel comp.py" to build glyphs which do not exist in the template or to rebuild accent glyphs which contain outlines.

"""

f = CurrentFont()
g = CurrentGlyph()

template_glyphs = f.lib['public.glyphOrder']
template_selection = f.templateSelection

if g is not None:
    Current_glyph_name = g.name
else:
    if len (template_selection) > 0:
        Current_glyph_name = template_selection[0]
    else:
        Current_glyph_name = 'No_current_glyph'

###### MARK OPTIONS ###############

import random

randombluegrey = (0.3,0.3,random.random(),0.8)

blue = (0,0,1,1)
green = (0,1,0,1)
yellow = (1,1,0,1)

markcolour = randombluegrey



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
	["aogonek","a","ogonek","bottom"],
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
	["eogonek","e","ogonek","bottom"],
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
	["iogonek","i","ogonek","bottom"],
	["imacron","dotlessi","macron","top"],
	["idotaccent","dotlessi","dotaccent","top"],
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
	["uogonek","u","ogonek","bottom"],
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
	
	## LOWERCASE ALTS ########################################
	["agrave.alt","a.alt","grave","top"],
	["aacute.alt","a.alt","acute","top"],
	["acircumflex.alt","a.alt","circumflex","top"],
	["atilde.alt","a.alt","tilde","top"],
	["adieresis.alt","a.alt","dieresis","top"],
	["amacron.alt","a.alt","macron","top"],
	["abreve.alt","a.alt","breve","top"],
	["aring.alt","a.alt","ring","top"],
	# aringacute.alt made manually
	["gcircumflex.alt","g.alt","circumflex","top"],
	["gcommaaccent.alt","g.alt","commaaccent.alt","top"],
	["gbreve.alt","g.alt","breve","top"],
	["gdotaccent.alt","g.alt","dotaccent","top"],
	
	## UPPERCASE ########################################
	["Agrave","A","grave.uc","top"],
	["Aacute","A","acute.uc","top"],
	["Acircumflex","A","circumflex.uc","top"],
	["Atilde","A","tilde.uc","top"],
	["Adieresis","A","dieresis.uc","top"],
	["Amacron","A","macron.uc","top"],
	["Abreve","A","breve.uc","top"],
	["Aring","A","ring.uc","top"],
	["AEacute","AE","acute.uc","top"],
	["Cacute","C","acute.uc","top"],
	["Cacute.pl","C","acute.ucpl","top"],
	["Ccircumflex","C","circumflex.uc","top"],
	["Ccaron","C","caron.uc","top"],
	["Cdotaccent","C","dotaccent.uc","top"],
	["Ccedilla","C","cedilla.uc","bottom"],
	["Dcaron","D","caron.uc","top"],
	["Egrave","E","grave.uc","top"],
	["Eacute","E","acute.uc","top"],
	["Ecircumflex","E","circumflex.uc","top"],
	["Ecaron","E","caron.uc","top"],
	["Edieresis","E","dieresis.uc","top"],
	["Emacron","E","macron.uc","top"],
	["Ebreve","E","breve.uc","top"],
	["Edotaccent","E","dotaccent.uc","top"],
	["Gcircumflex","G","circumflex.uc","top"],
	["Gbreve","G","breve.uc","top"],
	["Gdotaccent","G","dotaccent.uc","top"],
	["Gcommaaccent","G","commaaccent.uc","bottom"],
	["Hcircumflex","H","circumflex.uc","top"],
	["Igrave","I","grave.uc","top"],
	["Iacute","I","acute.uc","top"],
	["Icircumflex","I","circumflex.uc","top"],
	["Itilde","I","tilde.uc","top"],
	["Idieresis","I","dieresis.uc","top"],
	["Imacron","I","macron.uc","top"],
	["Ibreve","I","breve.uc","top"],
	["Idotaccent","I","dotaccent.uc","top"],
	["Jcircumflex","J","circumflex.uc","top"],
	["Kcommaaccent","K","commaaccent.uc","bottom"],
	["Lacute","L","acute.uc","top"],
	## Lcaron made manually
	["Lcommaaccent","L","commaaccent.uc","bottom"],
	## Ldot made manually
	["Nacute","N","acute.uc","top"],
	["Nacute.pl","N","acute.ucpl","top"],
	["Ncaron","N","caron.uc","top"],
	["Ntilde","N","tilde.uc","top"],
	["Ncommaaccent","N","commaaccent.uc","bottom"],
	["Ograve","O","grave.uc","top"],
	["Oacute","O","acute.uc","top"],
	["Oacute.pl","O","acute.ucpl","top"],
	["Ocircumflex","O","circumflex.uc","top"],
	["Otilde","O","tilde.uc","top"],
	["Odieresis","O","dieresis.uc","top"],
	["Omacron","O","macron.uc","top"],
	["Obreve","O","breve.uc","top"],
	["Ohungarumlaut","O","hungarumlaut.uc","top"],
	["Oslashacute","Oslash","acute.uc","top"],
	["Racute","R","acute.uc","top"],
	["Rcaron","R","caron.uc","top"],
	["Rcommaaccent","R","commaaccent.uc","bottom"],
	["Sacute","S","acute.uc","top"],
	["Sacute.pl","S","acute.ucpl","top"],
	["Scircumflex","S","circumflex.uc","top"],
	["Scaron","S","caron.uc","top"],
	["Scedilla","S","cedilla.uc","bottom"],
	["Scommaaccent","S","commaaccent.uc","bottom"],
	["Tcaron","T","caron.uc","top"],
	["Tcommaaccent","T","commaaccent.uc","bottom"],
	["uni021A","T","commaaccent.uc","bottom"],
	["Ugrave","U","grave.uc","top"],
	["Uacute","U","acute.uc","top"],
	["Ucircumflex","U","circumflex.uc","top"],
	["Utilde","U","tilde.uc","top"],
	["Udieresis","U","dieresis.uc","top"],
	["Umacron","U","macron.uc","top"],
	["Ubreve","U","breve.uc","top"],
	["Uring","U","ring.uc","top"],
	["Uhungarumlaut","U","hungarumlaut.uc","top"],
	["Wgrave","W","grave.uc","top"],
	["Wacute","W","acute.uc","top"],
	["Wcircumflex","W","circumflex.uc","top"],
	["Wdieresis","W","dieresis.uc","top"],
	["Ygrave","Y","grave.uc","top"],
	["Yacute","Y","acute.uc","top"],
	["Ycircumflex","Y","circumflex.uc","top"],
	["Ydieresis","Y","dieresis.uc","top"],
	["Zacute","Z","acute.uc","top"],
	["Zacute.pl","Z","acute.ucpl","top"],
	["Zcaron","Z","caron.uc","top"],
	["Zdotaccent","Z","dotaccent.uc","top"],

	### UPPERCASE ALTS ########################################
	
	["Wgrave.alt","W.alt","grave.uc","top"],
	["Wacute.alt","W.alt","acute.uc","top"],
	["Wcircumflex.alt","W.alt","circumflex.uc","top"],
	["Wdieresis.alt","W.alt","dieresis.uc","top"],	
		
	### SMALLCAPS ########################################
	["Agrave.sc","A.sc","grave","top"],
	["Aacute.sc","A.sc","acute","top"],
	["Acircumflex.sc","A.sc","circumflex","top"],
	["Atilde.sc","A.sc","tilde","top"],
	["Adieresis.sc","A.sc","dieresis","top"],
	["Amacron.sc","A.sc","macron","top"],
	["Abreve.sc","A.sc","breve","top"],
	["Aring.sc","A.sc","ring","top"],
	["AEacute.sc","AE.sc","acute","top"],
	["Cacute.sc","C.sc","acute","top"],
	["Cacute.scpl","C.sc","acute.pl","top"],
	["Ccircumflex.sc","C.sc","circumflex","top"],
	["Ccaron.sc","C.sc","caron","top"],
	["Cdotaccent.sc","C.sc","dotaccent","top"],
	["Ccedilla.sc","C.sc","cedilla","bottom"],
	["Dcaron.sc","D.sc","caron","top"],
	["Egrave.sc","E.sc","grave","top"],
	["Eacute.sc","E.sc","acute","top"],
	["Ecircumflex.sc","E.sc","circumflex","top"],
	["Ecaron.sc","E.sc","caron","top"],
	["Edieresis.sc","E.sc","dieresis","top"],
	["Emacron.sc","E.sc","macron","top"],
	["Ebreve.sc","E.sc","breve","top"],
	["Edotaccent.sc","E.sc","dotaccent","top"],
	["Gcircumflex.sc","G.sc","circumflex","top"],
	["Gbreve.sc","G.sc","breve","top"],
	["Gdotaccent.sc","G.sc","dotaccent","top"],
	["Gcommaaccent.sc","G.sc","commaaccent","bottom"],
	["Hcircumflex.sc","H.sc","circumflex","top"],
	["Igrave.sc","I.sc","grave","top"],
	["Iacute.sc","I.sc","acute","top"],
	["Icircumflex.sc","I.sc","circumflex","top"],
	["Itilde.sc","I.sc","tilde","top"],
	["Idieresis.sc","I.sc","dieresis","top"],
	["Imacron.sc","I.sc","macron","top"],
	["Ibreve.sc","I.sc","breve","top"],
	["Idotaccent.sc","I.sc","dotaccent","top"],
	["Jcircumflex.sc","J.sc","circumflex","top"],
	["Kcommaaccent.sc","K.sc","commaaccent","bottom"],
	["Lacute.sc","L.sc","acute","top"],
	## Lcaron.sc made manually
	["Lcommaaccent.sc","L.sc","commaaccent","bottom"],
	## Ldot.sc made manually
	["Nacute.sc","N.sc","acute","top"],
	["Nacute.scpl","N.sc","acute.pl","top"],
	["Ncaron.sc","N.sc","caron","top"],
	["Ntilde.sc","N.sc","tilde","top"],
	["Ncommaaccent.sc","N.sc","commaaccent","bottom"],
	["Ograve.sc","O.sc","grave","top"],
	["Oacute.sc","O.sc","acute","top"],
	["Oacute.scpl","O.sc","acute.pl","top"],
	["Ocircumflex.sc","O.sc","circumflex","top"],
	["Otilde.sc","O.sc","tilde","top"],
	["Odieresis.sc","O.sc","dieresis","top"],
	["Omacron.sc","O.sc","macron","top"],
	["Obreve.sc","O.sc","breve","top"],
	["Ohungarumlaut.sc","O.sc","hungarumlaut","top"],
	["Oslashacute.sc","Oslash.sc","acute","top"],
	["Racute.sc","R.sc","acute","top"],
	["Rcaron.sc","R.sc","caron","top"],
	["Rcommaaccent.sc","R.sc","commaaccent","bottom"],
	["Sacute.sc","S.sc","acute","top"],
	["Sacute.scpl","S.sc","acute.pl","top"],
	["Scircumflex.sc","S.sc","circumflex","top"],
	["Scaron.sc","S.sc","caron","top"],
	["Scedilla.sc","S.sc","cedilla","bottom"],
	["Scommaaccent.sc","S.sc","commaaccent","bottom"],
	["Tcaron.sc","T.sc","caron","top"],
	["Tcommaaccent.sc","T.sc","commaaccent","bottom"],
	["uni021A.sc","T.sc","commaaccent","bottom"],
	["Ugrave.sc","U.sc","grave","top"],
	["Uacute.sc","U.sc","acute","top"],
	["Ucircumflex.sc","U.sc","circumflex","top"],
	["Utilde.sc","U.sc","tilde","top"],
	["Udieresis.sc","U.sc","dieresis","top"],
	["Umacron.sc","U.sc","macron","top"],
	["Ubreve.sc","U.sc","breve","top"],
	["Uring.sc","U.sc","ring","top"],
	["Uhungarumlaut.sc","U.sc","hungarumlaut","top"],
	["Wgrave.sc","W.sc","grave","top"],
	["Wacute.sc","W.sc","acute","top"],
	["Wcircumflex.sc","W.sc","circumflex","top"],
	["Wdieresis.sc","W.sc","dieresis","top"],
	["Ygrave.sc","Y.sc","grave","top"],
	["Yacute.sc","Y.sc","acute","top"],
	["Ycircumflex.sc","Y.sc","circumflex","top"],
	["Ydieresis.sc","Y.sc","dieresis","top"],
	["Zacute.sc","Z.sc","acute","top"],
	["Zacute.scpl","Z.sc","acute.pl","top"],
	["Zcaron.sc","Z.sc","caron","top"],
	["Zdotaccent.sc","Z.sc","dotaccent","top"]

]


def build_accents(accent_list):
    if Current_glyph_name is not 'No_current_glyph':
        for glyph_name, base_comp, acc_comp, anchor in accent_list:
            if glyph_name == Current_glyph_name\
            or glyph_name in template_selection\
            or base_comp == Current_glyph_name\
            or base_comp in template_selection\
            or acc_comp == Current_glyph_name\
            or acc_comp in template_selection:

                query = []
                if glyph_name in f:
                    if len(f[glyph_name]) > 0: ## check for glyphs containing contours
                        query.append('skip')
                        print 'skipping', glyph_name, '- contains contours'
                if len(query) < 1:
                    if glyph_name in template_glyphs:
                        if acc_comp in f:
                            if len(f[acc_comp].anchors) > 0:
                                if base_comp in f:
                                    if len(f[acc_comp].anchors) > 0:
                                            AnchorList = []
                                            for a in f[base_comp].anchors:
                                                AnchorList.append(a.name)
                                            if anchor in AnchorList:
                                                parts = [(acc_comp, anchor)]
                                                result = f.compileGlyph(glyph_name, base_comp, parts)
                                                build_list.append(glyph_name)
                    else:
                        print 'skipping', glyph_name, 'not in template'
                else:
                    pass
        f.update()
    else:
        print "--------------------------------"
        print "No current glyph or template glyphs selected."


build_list = []

import datetime
now = datetime.datetime.now()
timestamp = now.strftime("%H-%M-%S")


build_accents(AccentList)

print "--------------------------------"
if len(build_list) < 1:
    print "Script did not yield any composites. Check base glyphs and anchors."
else:
    print "Building..."
    for glyph in build_list:
        print glyph
        f[glyph].mark = markcolour


print "--------------------------------"
if len(build_list) > 0:
    print"Accents built at " + str(timestamp)
