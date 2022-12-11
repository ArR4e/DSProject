kasutajanimi = input("Sisesta kasuatajanimi: ")

#https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
#https://stackoverflow.com/questions/57062794/how-to-check-if-a-string-has-any-special-characters/57062899
#https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
import re
import string

def has_numbers(inputString):
    #any(not c.isalnum() for c in parool1) == True:
    return bool(re.search(r'\d', inputString))

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Korda parooli: ")


    if parool1 != parool2:
        print("Viga paroolis! Sisestatud paroolid ei kattu!")
        continue
    if len(parool1) < 8:
        print("Viga paroolis! Sisestatud parool on lühem kui 8 tähemärki.")
        continue
    if any(not c.isalnum() for c in parool1) == True or parool1.isalnum() == True:
    #if parool1.isalnum() == True:
    #if has_numbers(parool1) == True:

        f = open("users.txt", "w")
        f.write(kasutajanimi + ":" + reverse(parool1) + "\n")
        f.close()
        break
    else:
        print("Viga paroolis! Parool ei sisalda numbreid!")
        continue
                        
      
    
    
