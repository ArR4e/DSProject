from math import ceil

pikkus = int(input("Palun sisesta elektriliini pikkus: "))
vahemaa = int(input("Palun sisesta kahe posti vaheline maksimaalne vahemaa: "))

postid = 1 + ceil(pikkus / vahemaa)

print("Liini ehitamiseks läheb vaja " + str(postid) + " posti.")