def poisse_ja_tüdrukuid(a):
    
    poisid = 0
    tudrukud = 0
    if a ==[]:
        return(poisid, tudrukud)
    if a[0]=="Kadri T":
        poisid -=1
        tudrukud -=2
    x = " ".join(a)
    if (x[0]) == "T":
        tudrukud -= 1
    poisid += x.count("P")
    tudrukud += x.count("T")
    if not a:
        return(poisid,tudrukud)
    else:
        return(poisid, tudrukud)