eesnimi = input("Sisesta oma eesnimi: ")
perenimi = input("Sisesta oma perenimi: ")

print("Sinu kasutajatunnus on: " + eesnimi.lower().replace('ä','a').replace('ö','o').
      replace('ü', 'y').replace('õ','o') + '.' + perenimi.lower().replace('ä','a').replace('ö', 'o').
      replace('ü','y').replace('õ','o'))
