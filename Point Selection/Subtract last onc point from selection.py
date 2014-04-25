import operator

g = CurrentGlyph()

## Collect selected on-curve points:

p_selected = []

for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j].onCurve.selected == True:
            p_selected.append((i,j))

## If no on-curve points are selected, look for off-curve points:

offCurve_selected = []

if len(p_selected) == 0:
    for i in range(len(g)):
        for j in range(len(g[i])):
            for n in g[i][j].offCurve:
                if n.selected == True:
                    offCurve_selected.append((i,j))
                    selected_segment = offCurve_selected[0]

## If only an off-curve point is selected, change selection to nearby on-curve point

                    g[selected_segment[0]][selected_segment[1]].onCurve.selected = True
                    p_selected.append(selected_segment)

if len(p_selected) == 0:
    print 'No points are selected'
else:
    ## Find which contour has the most points selected:

    cont_list = {}
    for pair in p_selected:
        if pair[0] not in cont_list:
            cont_list[pair[0]] = 1
        else:
            for q in cont_list:
                if q == pair[0]:
                    cont_list[pair[0]] = cont_list[pair[0]] + 1

    cont_num = max(cont_list.iteritems(), key=operator.itemgetter(1))[0]

    ## Collect selected points in relevant contour and deselect others:

    selected_points = []

    for p in p_selected:
        if p[0] == cont_num:
            selected_points.append(p)
        else:
            g[p[0]][p[1]].onCurve.selected = False
    
    ## List all possible points in relevant contour:

    contour_points = []
    for r in g[cont_num]:
        contour_points.append(r.onCurve)

    ## List indices of unselected points in relevant contour:

    unselected = []

    for i in range(len(g[cont_num])):
        if g[cont_num][i].onCurve.selected == False:
            unselected.append(i)
    
    ## Find which is last point in selection:
    
    if len(unselected) > 0:    
        if selected_points[-1][1] == (len(contour_points) - 1):
            p_last = unselected[0] - 1
        else:
            p_last = selected_points[-1][1]
    else:
        p_last = selected_points[-1][1]
    
    ## Subtract first point from selection:
    g[cont_num][p_last].onCurve.selected = False


g.update()