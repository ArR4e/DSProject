nimi=input("Sisesta kasutajanimi: ")


tagurpidi=""

while True:
    parool1=input("Sisesta parool: ")
    parool2=input("Sisesta parool uuesti: ")
    if parool1!=parool2:
        print("Paroolid ei kattu, proovi uuesti!","\n")
        continue
    if len(parool1)<8:
        print("Parool on liiga lühike, proovi uuesti!", "\n")
        continue
    tähed=0
    numbrid=0
    for sümbol in parool1:
        if sümbol.isdigit(): #tähtede ja numbrite eristamiseks https://stackoverflow.com/questions/24878174/how-to-count-digits-letters-spaces-for-a-string-in-python
            numbrid+=1
        if sümbol.isalpha():
            tähed+=1.
    if tähed<1 or numbrid <1:
        print("Parool peab sisaldama vähemalt ühte numbrit ja ühte tähte, proovi uuesti!","\n")
        continue
    break
    


for sümbol in parool1[::-1]: #tagurpidi sõne https://www.w3schools.com/python/python_howto_reverse_string.asp
    tagurpidi+=sümbol
            
f=open("users.txt","w")
f.write(nimi+":"+tagurpidi)
f.close()


    
