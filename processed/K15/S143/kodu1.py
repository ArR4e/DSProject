import re
with open("aadressid.txt","r") as f:
    l = list(map(lambda x: x.strip(),f.readlines()))
    nl = list(map(lambda y: y.split("~")[1].split("/")[0],list(filter(lambda x: re.match("^(http:){1}(/){2}(w){3}.ut.(e){2}/~(.)*$",x), l))))
    print("Kasutajanimed on: ")
    [print(x) for x in nl]