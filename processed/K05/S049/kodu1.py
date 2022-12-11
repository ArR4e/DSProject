kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool uuesti: ")
    if parool1 == parool2:
        if len(parool2) >= 8:
#https://stackoverflow.com/questions/19859282/check-if-a-string-contains-a-number
            if any(char.isdigit() for char in parool2) == True:
#https://careerkarma.com/blog/python-isalpha-isnumeric-isalnum/
                if any(char.isalpha() for char in parool2) == True:
                    break
    else:
        print("Teie paroolid ei ühti. Sisestage paroolid uuesti.")

        
  
        