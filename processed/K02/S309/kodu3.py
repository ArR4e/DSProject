#Küsime kasutajalt sisendid.
eesnimi = str(input("Palun sisestage enda eesnimi:"));
perenimi = str(input("Palun sisestage enda perenimi:"));

#moodustame kasutajanime
kasutajanimi = eesnimi.lower() + "." + perenimi.lower();

#kaotame kasutajanimes täpitähed
kasutajanimi = kasutajanimi.replace('ü','u');
kasutajanimi = kasutajanimi.replace('õ','o');
kasutajanimi = kasutajanimi.replace('ö','o');
kasutajanimi = kasutajanimi.replace('ä','a');

#väljastame kasutajanime
print(kasutajanimi);