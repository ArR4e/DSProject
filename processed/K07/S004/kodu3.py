kuud=["jaanuar","veebruar","märts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
def sünnikuupäev(ik):
    if ik[0]=="4" or ik[0]=="3":
        if ik[3]=="0":
            synd=ik[5:7],". ",kuud[int(ik[4])-1]," 19",ik[1:3]
        else:
            synd=ik[5:7],". ",kuud[int(ik[3:5])-1]," 19",ik[1:3]
        
    elif ik[0]=="5" or ik[0]=="6":
        if ik[3]=="0":
            synd=ik[5:7],". ",kuud[int(ik[4])-1]," 20",ik[1:3]
        else:
            synd=ik[5:7],". ",kuud[int(ik[3:5])-1]," 20",ik[1:3]
        
    else:
        if ik[3]=="0":
            synd=ik[5:7],". ",kuud[int(ik[4])-1]," 18",ik[1:3]
        else:
            synd=ik[5:7],". ",kuud[int(ik[3:5])-1]," 18",ik[1:3]

    return("".join(synd))
a=input("..")
print(sünnikuupäev(a))
    