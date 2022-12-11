with open("kinganumbrid.txt", "r") as file:
    lines = file.read().splitlines()
    list1 = []
    for kn in lines:
        for el in kn:
            if el.isdigit() or el == ".":
                pikkus = round(2/3*(float(kn)-2))
                list1.append(pikkus)
                break
            else:
                list1.append("Vigane sisend")
                break
for i in list1:
    print(i)
        
        