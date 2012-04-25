"""
This script opens an observer window and automatically updates the current space center window with glyphs which relate to the current glyph in the Glyph View window. Glyphs displayed in the space center are defined in the dictionary below and include base glyphs, accent glyphs, and all related composites.

This is an adaptation of Frederk Berlaen's MultiFontPreview observer.

NOTE: To stop this script you must close the observer window.

"""


import vanilla
from defconAppKit.windows.baseWindow import BaseWindowController
from defconAppKit.controls.glyphLineView import GlyphLineView
from mojo import events
from mojo.UI import *

font = CurrentFont()

AccentDict = {
"A" : ["A", "Agrave", "Aacute", "Acircumflex", "Atilde", "Adieresis", "Amacron", "Abreve", "Aring", "Aringacute", "Aogonek", "ogonek.uc", "grave.uc", "acute.uc", "circumflex.uc", "tilde.uc", "dieresis.uc", "macron.uc", "breve.uc", "ring.uc"],
"AE" : ["AE", "AEacute", "acute.uc"],
"C" : ["C", "Cacute", "Cacute.pl", "Ccircumflex", "Ccaron", "Cdotaccent", "Ccedilla", "cedilla.uc", "acute.uc", "acute.ucpl", "circumflex.uc", "caron.uc", "dotaccent.uc"],
"D" : ["D", "Dcaron", "caron.uc"],
"E" : ["E", "Egrave", "Eacute", "Ecircumflex", "Ecaron", "Edieresis", "Emacron", "Ebreve", "Edotaccent", "Eogonek", "ogonek.uc", "grave.uc", "acute.uc", "circumflex.uc", "caron.uc", "dieresis.uc", "macron.uc", "breve.uc", "dotaccent.uc"],
"G" : ["G", "Gcircumflex", "Gbreve", "Gdotaccent", "Gcommaaccent", "circumflex.uc", "breve.uc", "dotaccent.uc", "commaaccent.uc"],
"H" : ["H", "Hcircumflex", "circumflex.uc"],
"I" : ["I", "Igrave", "Iacute", "Icircumflex", "Itilde", "Idieresis", "Imacron", "Ibreve", "Idotaccent", "Iogonek", "ogonek.uc", "grave.uc", "acute.uc", "circumflex.uc", "tilde.uc", "dieresis.uc", "macron.uc", "breve.uc", "dotaccent.uc"],
"J" : ["J", "Jcircumflex", "circumflex.uc"],
"K" : ["K", "Kcommaaccent", "commaaccent.uc"],
"L" : ["L", "Lacute", "Lcaron", "Lcommaaccent", "Ldot", "acute.uc", "caron.uc", "dotaccent.uc", "commaaccent.uc"],
"N" : ["N", "Nacute", "Nacute.pl", "Ncaron", "Ntilde", "Ncommaaccent", "acute.uc", "acute.ucpl", "caron.uc", "tilde.uc", "commaaccent.uc"],
"O" : ["O", "Ograve", "Oacute", "Oacute.pl", "Ocircumflex", "Otilde", "Odieresis", "Omacron", "Obreve", "Ohungarumlaut", "grave.uc", "acute.uc", "acute.ucpl", "circumflex.uc", "tilde.uc", "dieresis.uc", "macron.uc", "breve.uc", "hungarumlaut.uc"],
"Oslash" : ["Oslash", "Oslashacute", "acute.uc"],
"R" : ["R", "Racute", "Rcaron", "Rcommaaccent", "acute.uc", "caron.uc", "commaaccent.uc"],
"S" : ["S", "Sacute", "Sacute.pl", "Scircumflex", "Scaron", "Scedilla", "Scommaaccent", "acute.uc", "acute.ucpl", "circumflex.uc", "caron.uc", "cedilla.uc", "commaaccent.uc"],
"T" : ["T", "Tcaron", "Tcommaaccent", "caron.uc", "commaaccent.uc"],
"U" : ["U", "Ugrave", "Uacute", "Ucircumflex", "Utilde", "Udieresis", "Umacron", "Ubreve", "Uring", "Uhungarumlaut", "Uogonek", "ogonek.uc", "grave.uc", "acute.uc", "circumflex.uc", "tilde.uc", "dieresis.uc", "macron.uc", "breve.uc", "ring.uc", "hungarumlaut.uc"],
"W" : ["W", "Wgrave", "Wacute", "Wcircumflex", "Wdieresis", "grave.uc", "acute.uc", "circumflex.uc", "dieresis.uc"],
"Y" : ["Y", "Ygrave", "Yacute", "Ycircumflex", "Ydieresis", "grave.uc", "acute.uc", "circumflex.uc", "dieresis.uc"],
"Z" : ["Z", "Zacute", "Zacute.pl", "Zcaron", "Zdotaccent", "acute.uc", "acute.ucpl", "caron.uc", "dotaccent.uc"],
"a" : ["a", "agrave", "aacute", "acircumflex", "atilde", "adieresis", "amacron", "abreve", "aring", "aringacute", "aogonek", "ogonek", "grave", "acute", "circumflex", "tilde", "dieresis", "macron", "breve", "ring"],
"ae" : ["ae", "aeacute", "acute"],
"c" : ["c", "cacute", "cacute.pl", "ccircumflex", "ccaron", "cdotaccent", "ccedilla", "cedilla", "acute", "acute.pl", "circumflex", "caron", "dotaccent"],
"d" : ["d", "dcaron", "caron.alt"],
"e" : ["e", "egrave", "eacute", "ecircumflex", "ecaron", "edieresis", "emacron", "ebreve", "edotaccent", "eogonek", "ogonek", "grave", "acute", "circumflex", "caron", "dieresis", "macron", "breve", "dotaccent"],
"g" : ["g", "gcircumflex", "gbreve", "gdotaccent", "gcommaaccent", "circumflex", "breve", "dotaccent", "commaaccent.alt"],
"h" : ["h", "hcircumflex", "circumflex.uc"],
"i" : ["i", "dotlessi", "igrave", "iacute", "icircumflex", "itilde", "idieresis", "imacron", "ibreve", "idotaccent", "iogonek", "ogonek", "grave", "acute", "circumflex", "tilde", "dieresis", "macron", "breve", "dotaccent"],
"dotlessi" : ["i", "dotlessi", "igrave", "iacute", "icircumflex", "itilde", "idieresis", "imacron", "ibreve", "idotaccent", "iogonek", "ogonek", "grave", "acute", "circumflex", "tilde", "dieresis", "macron", "breve", "dotaccent"],
"j" : ["j", "dotlessj", "jcircumflex", "circumflex"],
"dotlessj" : ["j", "dotlessj", "jcircumflex", "circumflex"],
"k" : ["k", "kcommaaccent", "commaaccent"],
"l" : ["l", "lacute", "lcaron", "lcommaaccent", "ldot", "acute", "caron.alt", "dotaccent", "commaaccent"],
"n" : ["n", "nacute", "nacute.pl", "ncaron", "ntilde", "ncommaaccent", "napostrophe", "acute", "acute.pl", "caron", "tilde", "commaaccent", "quoteright"],
"o" : ["o", "ograve", "oacute", "oacute.pl", "ocircumflex", "otilde", "odieresis", "omacron", "obreve", "ohungarumlaut", "grave", "acute", "acute.pl", "circumflex", "tilde", "dieresis", "macron", "breve", "hungarumlaut"],
"oslash" : ["oslash", "oslashacute", "acute"], 
"r" : ["r", "racute", "rcaron", "rcommaaccent", "acute", "caron", "commaaccent"],
"s" : ["s", "sacute", "sacute.pl", "scircumflex", "scaron", "scedilla", "scommaaccent", "cedilla", "acute", "acute.pl", "circumflex", "caron", "commaaccent"],
"t" : ["t", "tcaron", "tcommaaccent", "caron.alt", "commaaccent"],
"u" : ["u", "ugrave", "uacute", "ucircumflex", "utilde", "udieresis", "umacron", "ubreve", "uring", "uhungarumlaut", "uogonek", "ogonek", "grave", "acute", "circumflex", "tilde", "dieresis", "macron", "breve", "ring", "hungarumlaut"],
"w" : ["w", "wgrave", "wacute", "wcircumflex", "wdieresis", "grave", "acute", "circumflex", "dieresis"],
"y" : ["y", "ygrave", "yacute", "ycircumflex", "ydieresis", "grave", "acute", "circumflex", "dieresis"],
"z" : ["z", "zacute", "zacute.pl", "zcaron", "zdotaccent", "acute", "acute.pl", "caron", "dotaccent"],
"A.sc" : ["A.sc", "Agrave.sc", "Aacute.sc", "Acircumflex.sc", "Atilde.sc", "Adieresis.sc", "Amacron.sc", "Abreve.sc", "Aring.sc", "Aringacute.sc", "Aogonek.sc", "ogonek", "grave", "acute", "circumflex", "tilde", "dieresis", "macron", "breve", "ring"],
"AE.sc" : ["AE.sc", "AEacute.sc", "acute"],
"C.sc" : ["C.sc", "Cacute.sc", "Cacute.scpl", "Ccircumflex.sc", "Ccaron.sc", "Cdotaccent.sc", "Ccedilla.sc", "cedilla", "acute", "acute.pl", "circumflex", "caron", "dotaccent"],
"D.sc" : ["D.sc", "Dcaron.sc", "caron"],
"E.sc" : ["E.sc", "Egrave.sc", "Eacute.sc", "Ecircumflex.sc", "Ecaron.sc", "Edieresis.sc", "Emacron.sc", "Ebreve.sc", "Edotaccent.sc", "Eogonek.sc", "ogonek", "grave", "acute", "circumflex", "caron", "dieresis", "macron", "breve", "dotaccent"],
"G.sc" : ["G.sc", "Gcircumflex.sc", "Gbreve.sc", "Gdotaccent.sc", "Gcommaaccent.sc", "circumflex", "breve", "dotaccent", "commaaccent"],
"H.sc" : ["H.sc", "Hcircumflex.sc", "circumflex"],
"I.sc" : ["I.sc", "Igrave.sc", "Iacute.sc", "Icircumflex.sc", "Itilde.sc", "Idieresis.sc", "Imacron.sc", "Ibreve.sc", "Idotaccent.sc", "Iogonek.sc", "ogonek", "grave", "acute", "circumflex", "tilde", "dieresis", "macron", "breve", "dotaccent"],
"J.sc" : ["J.sc", "Jcircumflex.sc", "circumflex"],
"K.sc" : ["K.sc", "Kcommaaccent.sc", "commaaccent"],
"L.sc" : ["L.sc", "Lacute.sc", "Lcaron.sc", "Lcommaaccent.sc", "Ldot.sc", "acute", "caron.alt", "dotaccent", "commaaccent"],
"N.sc" : ["N.sc", "Nacute.sc", "Nacute.scpl", "Ncaron.sc", "Ntilde.sc", "Ncommaaccent.sc", "napostrophe.sc", "acute", "acute.pl", "caron", "tilde", "commaaccent", "quoteright"],
"O.sc" : ["O.sc", "Ograve.sc", "Oacute.sc", "Oacute.scpl", "Ocircumflex.sc", "Otilde.sc", "Odieresis.sc", "Omacron.sc", "Obreve.sc", "Ohungarumlaut.sc", "grave", "acute", "acute.pl", "circumflex", "tilde", "dieresis", "macron", "breve", "hungarumlaut"],
"Oslash.sc" : ["Oslashacute.sc"],
"R.sc" : ["R.sc", "Racute.sc", "Rcaron.sc", "Rcommaaccent.sc", "acute", "caron", "commaaccent"],
"S.sc" : ["S.sc", "Sacute.sc", "Sacute.scpl", "Scircumflex.sc", "Scaron.sc", "Scedilla.sc", "Scommaaccent.sc", "cedilla", "acute", "acute.pl", "circumflex", "caron", "commaaccent"],
"T.sc" : ["T.sc", "Tcaron.sc", "Tcommaaccent.sc", "caron", "commaaccent"],
"U.sc" : ["U.sc", "Ugrave.sc", "Uacute.sc", "Ucircumflex.sc", "Utilde.sc", "Udieresis.sc", "Umacron.sc", "Ubreve.sc", "Uring.sc", "Uhungarumlaut.sc", "Uogonek.sc", "ogonek", "grave", "acute", "circumflex", "tilde", "dieresis", "macron", "breve", "ring", "hungarumlaut"],
"W.sc" : ["W.sc", "Wgrave.sc", "Wacute.sc", "Wcircumflex.sc", "Wdieresis.sc", "grave", "acute", "circumflex", "dieresis"],
"Y.sc" : ["Y.sc", "Ygrave.sc", "Yacute.sc", "Ycircumflex.sc", "Ydieresis.sc", "grave", "acute", "circumflex", "dieresis"],
"Z.sc" : ["Z.sc", "Zacute.sc", "Zacute.scpl", "Zcaron.sc", "Zdotaccent.sc", "acute", "acute.pl", "caron", "dotaccent"],
"cedilla.uc" : ["cedilla.uc", "Ccedilla", "Scedilla", "C", "S"],
"ogonek.uc" : ["ogonek.uc", "Aogonek", "Eogonek", "Iogonek", "Uogonek", "A", "E", "I", "U"],
"grave.uc" : ["grave.uc", "Agrave", "Egrave", "Igrave", "Ograve", "Ugrave", "Wgrave", "Ygrave", "A", "E", "I", "U", "O", "W", "Y"],
"acute.uc" : ["acute.uc", "Aacute", "Aringacute", "AEacute", "Cacute", "Eacute", "Iacute", "Lacute", "Nacute", "Oacute", "Oslashacute", "Racute", "Sacute", "Uacute", "Wacute", "Yacute", "Zacute", "ring.uc", "A", "AE", "C", "E", "I", "L", "N", "O", "Oslash", "R", "S", "U", "W", "Y", "Z"],
"acute.ucpl" : ["acute.ucpl", "Cacute.pl", "Nacute.pl", "Oacute.pl", "Sacute.pl", "Zacute.pl", "C", "N", "O", "S", "Z"],
"circumflex.uc" : ["circumflex.uc", "Acircumflex", "Ccircumflex", "Ecircumflex", "Gcircumflex", "Hcircumflex", "Icircumflex", "Jcircumflex", "Ocircumflex", "Scircumflex", "Ucircumflex", "Wcircumflex", "Ycircumflex", "A", "C", "E", "G", "H", "I", "J", "O", "S", "U", "W", "Y"],
"caron.uc" : ["caron.uc", "Ccaron", "Dcaron", "Ecaron", "Ncaron", "Rcaron", "Scaron", "Tcaron", "Zcaron", "C", "D", "E", "N", "R", "S", "T", "Z"],
"caron.ucalt" : ["caron.ucalt", "Lcaron", "L"],
"tilde.uc" : ["tilde.uc", "Atilde", "Itilde", "Ntilde", "Otilde", "Utilde", "A", "I", "N", "O", "U"],
"dieresis.uc" : ["dieresis.uc", "Adieresis", "Edieresis", "Idieresis", "Odieresis", "Udieresis", "Wdieresis", "Ydieresis", "A", "E", "I", "U", "O", "W", "Y"],
"macron.uc" : ["macron.uc", "Amacron", "Emacron", "Imacron", "Omacron", "Umacron", "A", "E", "I", "O", "U"],
"breve.uc" : ["breve.uc", "Abreve", "Ebreve", "Gbreve", "Ibreve", "Obreve", "Ubreve", "A", "E", "G", "I", "O", "U"],
"ring.uc" : ["ring.uc", "Aring", "Aringacute", "Uring", "acute.uc", "A", "U"],
"hungarumlaut.uc" : ["hungarumlaut.uc", "Ohungarumlaut", "Uhungarumlaut", "O", "U"],
"dotaccent.uc" : ["dotaccent.uc", "Cdotaccent", "Edotaccent", "Gdotaccent", "Idotaccent", "Ldot", "Zdotaccent", "C", "E", "G", "I", "L", "Z"],
"commaaccent.uc" : ["commaaccent.uc", "Gcommaaccent", "Kcommaaccent", "Lcommaaccent", "Ncommaaccent", "Rcommaaccent", "Scommaaccent", "Tcommaaccent", "G", "K", "L", "N", "R", "S", "T"],
"cedilla" : ["cedilla", "ccedilla", "scedilla", "Ccedilla.sc", "Scedilla.sc", "C", "s", "C.sc", "S.sc"],
"ogonek" : ["ogonek", "aogonek", "eogonek", "iogonek", "uogonek", "Aogonek.sc", "Eogonek.sc", "Iogonek.sc", "Uogonek.sc", "a", "e", "i", "dotlessi", "u", "A.sc", "E.sc", "I.sc", "U.sc"],
"grave" : ["grave", "agrave", "egrave", "igrave", "ograve", "ugrave", "wgrave", "ygrave", "Agrave.sc", "Egrave.sc", "Igrave.sc", "Ograve.sc", "Ugrave.sc", "Wgrave.sc", "Ygrave.sc", "a", "e", "i", "dotlessi", "o", "u", "w", "y", "A.sc", "E.sc", "I.sc", "O.sc", "U.sc", "W.sc", "Y.sc"],
"acute" : ["acute", "aacute", "aringacute", "aeacute", "cacute", "eacute", "iacute", "lacute", "nacute", "oacute", "oslashacute", "racute", "sacute", "uacute", "wacute", "yacute", "zacute", "Aacute.sc", "Aringacute.sc", "AEacute.sc", "Cacute.sc", "Eacute.sc", "Iacute.sc", "Lacute.sc", "Nacute.sc", "Oacute.sc", "Oslashacute.sc", "Racute.sc", "Sacute.sc", "Uacute.sc", "Wacute.sc", "Yacute.sc", "Zacute.sc", "ring", "a", "c", "e", "i", "dotlessi", "l", "n", "o", "oslash", "r", "s", "u", "w", "y", "z", "A.sc", "C.sc", "E.sc", "I.sc", "L.sc", "N.sc", "O.sc", "Oslash.sc", "R.sc", "S.sc", "U.sc", "W.sc", "Y.sc", "Z.sc"],
"acute.pl" : ["acute.pl", "cacute.pl", "nacute.pl", "oacute.pl", "sacute.pl", "zacute.pl", "Cacute.scpl", "Nacute.scpl", "Oacute.scpl", "Sacute.scpl", "Zacute.scpl", "c", "n", "o", "s", "z", "C.sc", "N.sc", "O.sc", "S.sc", "Z.sc"],
"circumflex" : ["circumflex", "acircumflex", "ccircumflex", "ecircumflex", "gcircumflex", "hcircumflex", "icircumflex", "jcircumflex", "ocircumflex", "scircumflex", "ucircumflex", "wcircumflex", "ycircumflex", "Acircumflex.sc", "Ccircumflex.sc", "Ecircumflex.sc", "Gcircumflex.sc", "Hcircumflex.sc", "Icircumflex.sc", "Jcircumflex.sc", "Ocircumflex.sc", "Scircumflex.sc", "Ucircumflex.sc", "Wcircumflex.sc", "Ycircumflex.sc", "a", "c", "e", "g", "h", "i", "dotlessi", "j", "dotlessj", "o", "s", "A.sc", "C.sc", "E.sc", "G.sc", "H.sc", "I.sc", "J.sc", "O.sc", "S.sc"],
"caron" : ["caron", "ccaron", "ecaron", "ncaron", "rcaron", "scaron", "zcaron", "Ccaron.sc", "Dcaron.sc", "Ecaron.sc", "Ncaron.sc", "Rcaron.sc", "Scaron.sc", "Tcaron.sc", "Zcaron.sc", "c", "e", "n", "r", "s", "z", "C.sc", "D.sc", "E.sc", "N.sc", "R.sc", "S.sc", "T.sc", "Z.sc"],
"caron.alt" : ["caron.alt", "lcaron", "dcaron", "tcaron", "Lcaron.sc", "l", "d", "t", "L.sc"],
"tilde" : ["tilde", "atilde", "itilde", "ntilde", "otilde", "utilde", "Atilde.sc", "Itilde.sc", "Ntilde.sc", "Otilde.sc", "Utilde.sc", "a", "i", "dotlessi", "n", "o", "u", "A.sc", "I.sc", "N.sc", "O.sc", "U.sc"],
"dieresis" : ["dieresis", "adieresis", "edieresis", "idieresis", "odieresis", "udieresis", "wdieresis", "ydieresis", "Adieresis.sc", "Edieresis.sc", "Idieresis.sc", "Odieresis.sc", "Udieresis.sc", "Wdieresis.sc", "Ydieresis.sc", "a", "e", "i", "dotlessi", "o", "u", "w", "y", "A.sc", "E.sc", "I.sc", "O.sc", "U.sc", "W.sc", "Y.sc"],
"macron" : ["macron", "amacron", "emacron", "imacron", "omacron", "umacron", "Amacron.sc", "Emacron.sc", "Imacron.sc", "Omacron.sc", "Umacron.sc", "a", "e", "i", "dotlessi", "o", "u", "A.sc", "E.sc", "I.sc", "O.sc", "U.sc"],
"breve" : ["breve", "abreve", "ebreve", "gbreve", "ibreve", "obreve", "ubreve", "Abreve.sc", "Ebreve.sc", "Gbreve.sc", "Ibreve.sc", "Obreve.sc", "Ubreve.sc", "a", "e", "g", "i", "dotlessi", "o", "u", "A.sc", "E.sc", "G.sc", "I.sc", "O.sc", "U.sc"],
"ring" : ["ring", "aring", "aringacute", "uring", "Aring.sc", "Aringacute.sc", "Uring.sc", "ring", "a", "u", "A.sc", "U.sc"],
"hungarumlaut" : ["hungarumlaut", "ohungarumlaut", "uhungarumlaut", "Ohungarumlaut.sc", "Uhungarumlaut.sc", "o", "u", "O.sc", "U.sc"],
"dotaccent" : ["dotaccent", "cdotaccent", "edotaccent", "gdotaccent", "idotaccent", "ldot", "zdotaccent", "Cdotaccent.sc", "Edotaccent.sc", "Gdotaccent.sc", "Idotaccent.sc", "Ldot.sc", "Zdotaccent.sc", "c", "e", "g", "i", "dotlessi", "l", "z", "C.sc", "E.sc", "G.sc", "I.sc", "L.sc", "Z.sc"],
"commaaccent" : ["commaaccent", "kcommaaccent", "lcommaaccent", "ncommaaccent", "rcommaaccent", "scommaaccent", "tcommaaccent", "Gcommaaccent.sc", "Kcommaaccent.sc", "Lcommaaccent.sc", "Ncommaaccent.sc", "Rcommaaccent.sc", "Scommaaccent.sc", "Tcommaaccent.sc", "k", "l", "n", "r", "s", "t", "G.sc", "K.sc", "L.sc", "N.sc", "R.sc", "S.sc", "T.sc"],
"commaaccent.alt" : ["commaaccent.alt", "gcommaaccent", "g"],
"quoteright" : ["quoteright", "napostrophe", "napostrophe.sc", "n", "N.sc"]
}

class AccentPreview(BaseWindowController):

    def __init__(self):
        self.w = vanilla.Window((800, 400), minSize=(100, 100))
        self.w.glyphLineView = GlyphLineView((0, 0, 0, 0), pointSize=None, autohideScrollers=False, showPointSizePlacard=True)
        events.addObserver(self, "glyphChanged", "currentGlyphChanged")
        self.glyphChanged(dict(glyph=CurrentGlyph()))
        self.setUpBaseWindowBehavior()
        self.w.open()

    def windowCloseCallback(self, sender):
        events.removeObserver(self, "currentGlyphChanged")
        super(AccentPreview, self).windowCloseCallback(sender)

    def glyphChanged(self, info):
        glyphs = []
        glyph = info["glyph"]
        if glyph is None:
            glyphs = []
        else:
            glyphName = glyph.name
            if glyphName in AccentDict:
                glyphList = AccentDict[glyphName]
                glyphs = [font[glyphName].naked() for glyphName in glyphList if glyphName in font]
                SC = CurrentSpaceCenter()
                if SC is not None:
                    CurrentSpaceCenter().set(glyphList)
                
        self.w.glyphLineView.set(glyphs)

AccentPreview()