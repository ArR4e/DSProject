def moos(a, b, c):
    n = 0
    while True:
        if c >= 5 and a >= 1:
            c = c - 5
            a = a - 1
            n = n + 1
        else:
            break
    while True:
        if c > 0 and b >= 1:
            c = c - 1
            b = b - 1
            n = n + 1
        else:
            break
    if c == 0:
        return n
    else:
        return -1
        

print("Palun kirjutage üles suurte karpide, väikeste karpide ja mooside arv kilogrammides.")
print("Suurde karpi mahub 5 kg moosi, väikesesse karpi aga 1 kg moosi.")
print("Alustuseks kasutab tüdruk suuri karpe ja seejärel väikseid.")
print("Kui karpe ei ole piisavalt, siis ei tee Emma moosi.")

suuredKarbid = int(input("Palun kirjutage suurte karpide arvu: "))
väiksedKarbid = int(input("Palun kirjutage väikeste karpide arvu: "))
kogus = int(input("Palun kirjutage keedetava moosi koguse (kg): "))

moos(suuredKarbid, väiksedKarbid, kogus)


