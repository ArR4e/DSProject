nimi=input(str("Sisesta kasutajanimi: "))
parool1=input(str("Sisesta salasõna: "))
parool2=input(str("Sisesta salasõna uuesti: "))
if parool1!=parool2:
    print("Parool ei ole sobiv, palun sisesta parool uuesti")
    len(parool2)
elif len(parool2)<8:
    print("Parool ei ole sobiv, palun sisesta parool uuesti")
elif (not parool2.isalnum()) and parool2.isalpha() or parool2.isnumeric()==True:
    print("Parool ei ole sobiv, palun sisesta parool uuesti")
else:
    f=open("users.txt")
    tagurpidi1=parool2[::-1]
    tagurpidi2=nimi[::-1]
    f.writelines(tagurpidi1 + tagurpidi2)
    f.close