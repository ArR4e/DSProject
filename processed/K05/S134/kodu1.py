kasutajanimi = input("Sisestage kasutajanimi: ")
parool = input("Sisestage parool: ")
parool2 = input("Sisestage parool uuesti: ")
def num_there(s):
    return any(i.isdigit() for i in s)

if parool != parool2:
    print("Paroolid ei kattu")
else:
    if len(parool) < 8:
        print("Paroolis pole vähemalt 8 tähemärki")
    else:
        if str.lower(parool) or str.upper(parool) and str.islower(parool) or str.isupper(parool) and num_there(parool):
            reversed = ''.join(reversed(parool))
            f = open("users.txt", "w")
            f.write(kasutajanimi + ":")
            f.write(reversed)
            f.close()
        else:
            print("Paroolis pole vähemalt ühte numbrit ja tähte.")
        
    
        