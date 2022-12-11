Liin=float(input("Sisesta liini pikkus:"))
Maxpikkus=float(input("Sisesta postidevaheline maksimaalne kaugus:"))
if Liin % Maxpikkus == 0:
    print("Miinimum postide arv:", 1 +  Liin // Maxpikkus)
else:
    if Liin % Maxpikkus > 0 or Liin % Maxpikkus < 1:
        print("Miinimum postide arv:", 2 + Liin // Maxpikkus)
            
        
  