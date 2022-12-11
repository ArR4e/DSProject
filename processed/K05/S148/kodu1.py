def f(a, b, c):
    if (b == c) and (len(b) >= 8) and g(b) == h(b) == True:
        return True
    else:
        return False

def g(b):
    for e in b:
        if e.isalpha():
            return True
    return False

def h(b):
    for e in b:
        if e.isdigit():
            return True
    return False

kasutaja = input("Sisesta kasutajanimi: ")

while True:
    parool_1 = input("Sisesta parool: ")
    parool_2 = input("Sisesta parool uuesti: ")
    
    if f(kasutaja, parool_1, parool_2) == True:
        break
    else:
        print("Proovi uuesti")

f = open("users.txt", "w")
f.writelines(kasutaja + ":" + parool_1[::-1])
f.close()