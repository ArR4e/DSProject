def nr_to_pikkus(kinganumber):
    return round(2/3 * (kinganumber - 2))

with open("kinganumbrid.txt", 'r') as f:   
    for rida in f:
        try:
            number = float(rida)
            print(nr_to_pikkus(number))
        except:
            print("Vigane sisend")
            
