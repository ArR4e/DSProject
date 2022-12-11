f = open("kinganumbrid.txt", "r", encoding = "UTF-8")

for rida in f:
    try:
        jl_pikkus = round(2/3*(float(rida)-2))
        print(jl_pikkus)
    except:
        print("Vigane sisend")
        