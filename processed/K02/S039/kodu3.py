eesnimi=input("Sinu eesnimi: ")
perenimi=input("Sinu perekonnanimi: ")
kasutaja=str(eesnimi+"."+perenimi).lower().replace('ä','a').replace('õ','o').replace('ü','u').replace('ö','o')
print(kasutaja)