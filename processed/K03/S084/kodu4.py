#Avab faili
with open("kinganumbrid.txt", "r") as file:
    #Võtab ridade listi ja käib kõik read ükshaaval läbi
    lines = file.readlines()
    for line in lines:
        #Vaatab kas tegemist on arvuga
        try:
            #Eemaldab realõpu ja arvutab jalapikkuse
            arv = float(line.strip())
            jalg = round(2 / 3 * (arv - 2))
            print(jalg)
        except:
            #Kui reas pole arv, siis annab teate
            print("Vigane sisend")