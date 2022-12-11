def silu_andmed(a,b):
    counter = 1
    counter_3 = 1
    new_list = []
    counter_4 = b
    for i in a:
        element = 0
        counter_2 = counter_3 - 1
        counter_4 = b
        while counter_2 >= 0 and counter_4 > 0:
            element += 1/float(a[counter_2])
            counter_2 -=1
            counter_4 -= 1
        new_list += [counter/(element)]
        if counter < b:
            counter += 1
        counter_3 += 1
    return new_list


aktsiad = []
f = open("aktsiad.txt")
for x in f:
    aktsiad += [x.split()[3]]
f.close()

print(aktsiad)
print(silu_andmed(aktsiad,50))