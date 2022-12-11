import re

f = open("aadressid.txt",'r')
print("Kasutajanimed on:")

while True:
    x = (f.readline()).strip('\n')
    if x == '':
        break
    if re.match('http://www.ut.ee/~.*',x):
        print(x[18:22])
    
    
    
    
    
    
f.close()