def poisse_ja_tüdrukuid(a):
    t=0
    p=0
    for ele in a:
        ele=ele.split()
        for s6na in ele:
            if s6na=="T":
                t+=1
            if s6na=="P":
                p+=1
    return (p, t)   