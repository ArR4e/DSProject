nimi = str(input("Palun sisesta oma nimi: "))
esparool = str(input("Palun sisesta oma parooli: "))
teisparool = str(input("Palun korda oma parooli: "))
while True:
    if esparool != teisparool:
        print("Esimene parool ei kattu teisega ")
        esparool = input("Palun sisesta oma parooli: ")
    if len(str(esparool)) < 8:
        print("Teie parool on lühem, kui 8 tähemärki ")
        esparool = input("Palun sisesta oma parooli: ")
    if esparool.isalpha() or esparool.isdigit():
        print("Teie parool ei tohi sisaldada ainult tähte või ainult numbre ")
        esparool = input("Palun sisesta oma parooli: ")
    else:
        text = str(esparool)[::-1]
        print(text)
        break
f = open("users.txt", "w")
a = nimi + ":" + text
f.write(a)
f.close()
        


    
