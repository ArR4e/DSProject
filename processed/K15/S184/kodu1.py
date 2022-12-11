import re

fail="aadressid.txt"
f=open(fail, encoding="utf-8")
for rida in f:
    var = re.search("http://www.ut.ee/~([A-Za-z_0-9.-]+).*", rida)
    if var:
        print(var.group(1)) 

f.close()
