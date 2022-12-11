import random
import string
a=[]
for x in string.punctuation:
    a.append(x)
def suurväike(sisend):
    väljund=""
    b=a[random.randint(0,len(a)-1)]
    for x in sisend:
        if x.isupper():
            väljund += x.lower()
        if x.islower():
            väljund += x.upper()
        if x == " ":
            väljund += " "
        if (x in a):
            väljund += b
    return(väljund)
print(suurväike("dsa dasdas ...."))