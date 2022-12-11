from string import *

def parool(a, b):
    if a==b:
        return True
    else:
        print("Paroolid ei ühti.")
        return False

##kontrollib sõne pikkust
def piisav_pikkus(l):
    if len(l) >= 8:
        return True
    else:
        print("Parool peab olema vähemalt 8-kohaline.")
        return False


def piisavalt_raske(b):
    ## nii sümbolid kui ka tähed loeatakse samaks => kui parool sisaldab lisaks numbritele ka tähti või sümboleid siis on see piisav
    if (sisaldab_tähti(b) or sisaldab_sumboleid(b)) and sisaldab_nr(b):
        return True
    else:
        print("Parool peab sisaldama nii tähti kui ka numbreid.")


##funktsioonid sõne sisu kontrollimiseks
def sisaldab_sumboleid(s):
    for i in punctuation:
        if i in s:
            return True
def sisaldab_tähti(t):
    for i in ascii_letters:
        if i in t:
            return True
def sisaldab_nr(n):
    for i in digits:
        if i in n:
            return True

##sõne ümber pööramine
def parool_flip(f):
    rev = []
    e = ""
    for i in f:
        rev.append(i)
    rev.reverse()
    for i in rev:
        e += i
    return e    
    
    
def main():
    a = input("Sisestage kasutaja nimi: ")
    while(True):
        b = input("Sisestage parool: ")
        c = input("Sisestage parool teistkorda: ")
        if parool(b, c) and piisav_pikkus(b) and piisavalt_raske(b):
            print("Parool on piisavalt tugev.")
            break
    b = parool_flip(b)
    f = open("users.txt", "a")
    f.write(a + ":" + b + "\n")
    f.close()
main()