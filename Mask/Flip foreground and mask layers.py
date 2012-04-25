g = CurrentGlyph()

g.prepareUndo('flip foreground mask layers')
g.flipLayers("foreground", "mask")
g.performUndo()
g.update()