def küsi_parool():
    parool1 = input("Sisesta parool 1. korda: ")
    parool2 = input("Sisesta parool 2. korda: ")
    return parool1, parool2

def on_täht_ja_number(parool):
    on_täht = 0
    on_number = 0
    on_sümbol = 0
    for s in parool:
        if s.isalpha():
            on_täht +=1
        elif s.isdecimal():
            on_number +=1
        elif s.isprintable():
            on_sümbol += 1
        else: return False
    return on_täht !=0 and (on_number + on_sümbol) != 0 

kasutajanimi = input("Sisesta kasutajanimi: ")
parool1, parool2 = küsi_parool()

while True:
    if parool1 != parool2:
        print("Sisestatud paroolid ei kattu, proovi uuesti")
        parool1, parool2 = küsi_parool()
    elif len(parool1)<8:
        print("Parool on liiga lühike, proovi uuesti")
        parool1, parool2 = küsi_parool()
    elif not on_täht_ja_number(parool1):
        print("Parool peab sisaldama tähti ja numbreid, proovi uuesti")
        parool1, parool2 = küsi_parool()
    else:
      #  print(parool1)
        break

parool_tagurpidi = parool1[::-1] #https://www.w3schools.com/python/python_howto_reverse_string.asp
#print(parool_tagurpidi)

f = open("users.txt", "w")
f.write(kasutajanimi+":"+parool_tagurpidi)
f.close()
