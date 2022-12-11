f=open("aadressid.txt",encoding="UTF-8")
sisu=f.readlines()
f.close()
vastus=[]
for a in sisu:
    if "http://www.ut.ee" in a:
        if "~" in a:
            asi=a.split("/")
            for b in asi:
                if "~" in b:
                    vastus.append(b)
for a in range(len(vastus)):
    vastus[a]=vastus[a].strip("~")
    print(vastus[a])