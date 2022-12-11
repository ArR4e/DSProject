fail_1 = input("fail 1: ")
fail_2 = input("fail 2: ")
f1 = open(fail_1)
f2 = open(fail_2, "w")

loe = f1.read()
counter = loe.count("Hello")
asendus = loe.replace("Hello", "Tere")
print(asendus)

uus = f2.write(asendus)
f1.close()

print(counter)
f2.close()