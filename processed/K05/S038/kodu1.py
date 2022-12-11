nimi=input("Sisestage kasutajanimi:")
def number(v):
    for i in v:
        if i.isdigit():
            return True
    return False
def f(x):
    return x[::-1]

while True:
    a=input("Sisestage parool:")
    b=input("Sisestage parool uuesti:")
    if str(a)== str(b):
        if len(a)>= 8:
            if number(a)== True:
                e=f(a)
                break
            else:
                print("Paroolis peavad olema nii t2hed kui numbrid!")
        else:
            print("Parool on liiga lyhike!")
    else:
        print("Paroolid ei yhildu!")
fail=open("users.txt","w+")
L=[nimi,":",e]
fail.writelines(L)
fail.close()

    