def moos(suurkarp, vaikekarp, kogus):
    karbid=0
    while True:
        if kogus >= 5 and suurkarp > 0 :
            suurkarp -= 1; karbid+= 1; kogus-=5
        elif 0 < kogus < 5 and vaikekarp > 0:
            vaikekarp -=1; karbid += 1; kogus -= 1
        elif kogus == 0:
            return karbid
        else:
            return -1
        
suur=int(input("palju suuri karpe on?: "))     
vaike=int(input("palju vaikeseid karpe on?: "))
kg=int(input("palju moosi on?: "))

print(moos(suur,vaike,kg))