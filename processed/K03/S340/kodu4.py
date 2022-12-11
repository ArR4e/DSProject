g = open('kinganumbrid.txt')
esimene = g.readline()
teine = g.readline()
kolmas = g.readline()
neljas = g.readline()
try:
    esimene1 = round((int(esimene)-2)*2/3)
except:
    esimene1 = ("Vigane sisend")
try:    
    teine1 = round((float(teine)-2)*2/3)
except:
    teine1 = ("Vigane sisend")
try:
    kolmas1 = round((int(kolmas)-2)*2/3)
except:
    kolmas1 = ("Vigane sisend")
try:
    neljas1 = round((int(neljas)-2)*2/3)
except:
    neljas1 = ("Vigane sisend")
print(esimene1 , teine1 , kolmas1 , neljas1, sep='\n')
