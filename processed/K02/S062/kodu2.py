liin=int(input("Sisesta ehitatava elektriliini pikkus:"))
maks_kaugus=int(input("Sisesta maksimaalne kahe kõrvuti asuva posti vaheline kaugus:"))
vastus=1+(liin+maks_kaugus-1)//maks_kaugus
print(vastus)