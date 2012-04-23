glyph = CurrentGlyph()

Selected_nodes_x = []
Selected_nodes_y = []

for contour in glyph:
    for node in contour.points:
        if node.selected == True:
            Selected_nodes_x.append(node.x)
            Selected_nodes_y.append(node.y)

if len(Selected_nodes_x) > 1:
    xMax = max(Selected_nodes_x)
    yMax = max(Selected_nodes_y)
    xMin = min(Selected_nodes_x)
    yMin = min(Selected_nodes_y)

    xMid = int(round(xMin + (xMax - xMin)/2))
    yMid = int(round(yMin + (yMax - yMin)/2))

    glyph.addGuide((xMid, yMid), 90, name="mid")

else:
    print "Please select two or more nodes."