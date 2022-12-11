x = input("Sisesta sõne: ")
uus = ""

def suurväike(x):
    return uus
    
for täht in x:
    if (täht.isupper()) == True:
        uus += (täht.lower())
    elif (täht.islower()) == True:
        uus += (täht.upper())
    elif (täht.isspace()) == True:
        uus += täht
    else:
        for i in ('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'):
            if(täht == i):
                uus += "&"
            break
              
print(suurväike(x))
        