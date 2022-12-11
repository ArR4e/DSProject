fileOlemas = input("Gimme file 1: ")
fileUus = input("Gimme new file name: ")

f1 = open(fileOlemas, "r")
f2 = open(fileUus, "w")

read = f1.readlines()

counter = 0
#print(read)
for el in read:
    counter += el.count("Hello")
    new = el.replace("Hello", "Tere")
    f2.write(new)
    
print(counter)
f1.close()
f2.close()