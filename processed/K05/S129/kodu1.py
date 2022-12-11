#reverse "string"[::-1]  (extended slice syntax)
import string


tähed = set(list(string.ascii_letters))
numbers = set(list(string.digits))


kasutajanimi = str(input('Sisesta kasutajanimi: '))


while True:
    parool1 = str(input('Sisesta parool esimest korda: '))
    parool2 = str(input('Sisesta parool teist korda: '))
    
    if parool2 != parool1:
        print('Paroolid ei kattu')
        continue
    
    if len(parool1) < 8:
        print('Parool on liiga lühike')
        continue
        
    chars = set(list(parool1))
    
    if not tähed.intersection(chars):
        print("Parool peab sisaldama tähti ja numbreid")
        continue
    
    if not numbers.intersection(chars):
        print('Parool peab sisaldama vähemalt ühte numbrit')
        continue
    
    
    parool = parool1[::-1]
    break


with open('users.txt', 'a') as users:
    users.write(f"{kasutajanimi}:{parool}")
    
users.close()




