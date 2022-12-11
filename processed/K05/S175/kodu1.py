kasutajanimi = input("Sisesta kasutajanimi: ")
parool = input("Sisesta parool: ")
parool2 = input("Sisesta parool uuesti: ")
reversed=''.join(reversed(parool))
 
def tähemärgid_loend(parool):
    tähemärgid = 0
    for i in parool:
        if i.isdigit():
            tähemärgid+=1
            return tähemärgid
    
if parool == parool2:
    tähemärgid_loend(parool)
else:
    print("Paroolid ei kattu, proovi uuesti.")
if tähemärgid_loend(parool) >= 8:
    for character in parool:
        if character.isdigit():
            contains_digit = True
        else:
            print("Paroolid ei sobi, lisa numbreid või teek see pikemaks ja proovi uuesti.")


    
tekstifail = open("users.txt", "w")
tekstifail.write( kasutajanimi + ":" + reversed )             
tekstifail.close()       
    
        
