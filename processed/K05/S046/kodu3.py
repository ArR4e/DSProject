#a = suur
#b=väike
#c=kogus
def moos(a,b,c):
    vajasuuri = c // 5
    if vajasuuri > a:
        vajaväikseid = c - a*5
        if vajaväikseid > b:
            return(-1)
        else:
            return(a+vajaväikseid)
    else:
        vajaväikseid = c - vajasuuri*5
        if vajaväikseid > b:
            return(-1)
        else:
            return(vajasuuri+vajaväikseid)

print(moos(5, 1, 9))