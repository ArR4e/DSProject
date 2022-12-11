#küsime kasutajalt failinimed
fail1nimi = str(input("Sisestage lähtefaili nimi: "));
fail2nimi = str(input("Sisestage sihtfaili nimi: "));


#loeme sisse lähtefaili andmed
with open((fail1nimi), "r") as file1:
    file1andmed = file1.read();

#loeme üle vahetatavate sõnade koguse et seda hiljem kasutajale printida
#lisaks teostame sõnade vahetuse
vahetatudkogus = file1andmed.count("Hello");
file1andmed = file1andmed.replace("Hello", "Tere");

#kirjutame muudetud andmed sihtfaili
with open(fail2nimi, "w") as file2:
    file2.write(file1andmed);
    
#prindime eelnevalt loetud vahetatud sõnade koguse
print(vahetatudkogus);