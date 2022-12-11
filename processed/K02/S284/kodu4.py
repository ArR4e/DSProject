file_1 = input("Sisesta ingliskeelse faili nimi: ")
file_2 = input("Sisesta eestikeelse faili nimi: ")

f1 = open('file_1', "r", encoding = "UTF-8").replace("Hello", "Tere")
f2 = open('file_2', "w", encoding = "UTF-8")

from file_2.count("Tere")

file_1.close()
file_2.close()

print('count')









