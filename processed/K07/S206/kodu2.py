
pikkus = float(input("Sisesta teepikkus kilomeetrites: "))
def hind(rida, pikkus):
    rida = rida.split(",")
    return (float(rida[-2]) + pikkus*float(rida[-1]), rida[0])
    
with open("taksohinnad.txt", encoding="UTF-8") as f:
    hinnad = []
    try:
        for rida in f:
            hinnad.append(hind(rida.strip(), pikkus))
        odavaim = hinnad[hinnad.index(min(hinnad))][1]
        if odavaim == "Sõps veab":
            print (f"Kõige odavam on kui {odavaim}.")
        else:
            print(f"Kõige odavam on {odavaim}.")
    except:
        print("tühi fail")