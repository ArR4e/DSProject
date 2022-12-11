import math

liin = input("Kui pikk on liin? Sisesta täisarv: ")
l = int(liin)
postid = input("Kui suur on maksimaalne kahe posti vahe? Sisesta täisarv: ")
p = int(postid)

print("Poste kulub: ", math.ceil(l/p + 1))