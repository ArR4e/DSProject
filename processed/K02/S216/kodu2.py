
liini_pikkus = int(input("Sisestage on liini pikkus meetrites: "))
postidekaugus = int(input("Sisestage postide maksimaalkaugus: "))
postid = 1
postidekaugus2 = 0
# nt 400m liin ja 40m vahelt on post.
# poste oleks siis 1 + 10 = 11 kuna post on alguses ja lõpus
# Kui aga kaugus on pikem nt 401m siis oleks 12 posti.

while postidekaugus2 < liini_pikkus:
    postidekaugus2 = postidekaugus + postidekaugus2
    postid = postid + 1

print("Poste on kokku " + str(postid))








