import re
s =[]
fail = open("aadressid.txt","r", encoding="UTF-8")
for rida in fail:
    if re.match(".*http://www.ut.ee/",rida):
        x = re.findall("/~\w*",rida)
        s.append(x)
    else:
        continue
for i in s:
    nimi = ""
    for k in i:
        for j in k:
            if j == "~" or j == "'" or j == "/":
                continue
            else:
                nimi += str(j)
        print(nimi)


