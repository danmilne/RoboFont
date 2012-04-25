g = CurrentGlyph()

for guide in g.guides:
    if guide.name == "mid":
        g.removeGuide(guide)