import re
muster="http://www.ut.ee/~+[a-zA-Z0-9_]+/+.*"
f=open('aadressid.txt',encoding='UTF-8')
for rida in f:
    if re.search(muster,rida):
        rid=rida.strip().split('/')
        nimi=rid[3].strip('~')
        print(nimi)
