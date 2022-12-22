def cloplst(firstlist):
    wow = [[]]
    for i in firstlist:
        wow.append([firstlist[i]])
        secondlist = []
        for j in wow:
            secondlist.append(j)
        wow.append(secondlist)
        return wow


cloplst([1, 2, 3, 4, 25])
