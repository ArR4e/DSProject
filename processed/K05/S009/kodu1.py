def registreerumine():
        kasutajanimi = input("Palun vali kasutajanimi: ")
        parool = input("Palun sisesta parool: ")
        parool_uuesti = input("Palun sisesta parool uuesti: ")
        
        While True:
            if parool == parool_uuesti True:
                return
            elif len(parool) >= 8 True:
                return
            elif parool.isalnum() == True:
                return
            #vihje Googeldatud: https://careerkarma.com/blog/python-isalpha-isnumeric-isalnum
            print(parool[::-1])
            #vihje Googeldatud: https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
            
            f = open("users.txt", "w")
            f.write("kasutajanimi: " + kasutajanimi + "\n")
            f.write("parool: " + parool + "\n")
            f.close
        
        else:
            print("Teie paroolid ei kattu. Proovige uuesti")
            
print(registreerumine())


    
    