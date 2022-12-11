x = int(input( "Palun sisesta elektriliini pikkus meetrites: "))
y = int(input( "Palun sisesta liinidevaheline kaugus meetrites: "))
z = str(round(x/y + 2))
print("Elektriliini paigaldamiseks läheb vaja vähemalt " + z + " posti.")