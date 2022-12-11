def sünnikuupäev(id):
    a=id[1:3]
    k=id[3:5]
    p=id[5:7]
    
    kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    k=kuud[int(k)-1]
    
    if id[0]=="3" or id[0]=="4":
        a="19"+a
    elif id[0]=="5" or id[0]=="6":
        a="20"+a
    elif id[0]=="7" or id[0]=="8":
        a="21"+a
    elif id[0]=="1" or id[0]=="2":
        a="18"+a
    
    return(p+". "+k+ " " +a)