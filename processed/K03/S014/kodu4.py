import time #sest mu except jääb järjekindlalt loopima
#ja ma tahan, et ta seda vähemalt aeglasemalt teeks
#et ma jõuaksin breaki sisestada
#enne kui silme eest kirjuks läheb

f=open("kinganumbrid.txt")

while True:
    try:
        kinganumber=float(f.readline())
        jalalaba=float(round(2/3*(kinganumber-2),2))
        print(jalalaba)
        
    except:
        print("Paha lugu, failis on midagi käest läinud. Ehk kirjutasid sinna mõne arvu asemele hoopis lemmikpoliitiku nime? Kontrolli üle, kas failis on kõik ikka arvud!")
        time.sleep(3)
         #sest exceptist ma ei saa trysse tagasi ja muidu tuleb hullunud loop, kuni jõuan breaki sisestada
         #sleep aitab erinevaid koode katsetada, hullumiseta
        break
f.close()
    
print("Jooksis lõpuni, jee!")
#et ma saaks aru, kas vaatas faili lõpuni üle
    
    

    

