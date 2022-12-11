nimi=str(input("Sisesta kasutajanimi: "))

def has_numbers(a):
    return any(char.isdigit() for char in a)


while True:

    parool=str(input("Sisesta parool: "))
    parool2=str(input("Sisesta parool uuesti: "))
    
    if parool != parool2:
        continue
    elif len(parool)<8:
        continue
    elif has_numbers(parool)!=True:
        continue
    else:
        break

parool=parool[::-1]

f=open("users.txt", "x")
fail=f.write(nimi+":"+parool)

f.close()
    
    
