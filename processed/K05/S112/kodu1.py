kasutajanimi = input("Sisesta kasutajanimi: ")

while True:
    parool1 = str(input("Sisesta parool: "))
    parool2 = str(input("Sisesta parool uuesti: "))
    if parool1 == parool2:
        if len(parool1) >= 8:
            numbrid = any(c.isdigit() for c in parool1)
            if numbrid == True:
                break
            else:
                print("Parool on puudulik.")
                continue
        else:
            print("Parool on puudulik.")
            continue
    else:
        print("Parool on puudulik.")
        continue

def f(x):
    return x[::-1]

ümberpöörd = f(parool1)

fail = open("users.txt","w")
fail.write(kasutajanimi + ":" + ümberpöörd)

fail.close()

        
    
        