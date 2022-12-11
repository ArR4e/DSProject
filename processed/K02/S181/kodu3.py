try:
    eesnimi = input("Sisesta eesnimi: ").lower()
    perenimi = input("Sisesta perenimi: ").lower()
    kasutaja = eesnimi+"."+perenimi
    print(kasutaja)
except:
    print("error")