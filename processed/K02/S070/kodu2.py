import math 
print("Sirgjoonelise elektriliini ehitamisel paigutatakse kõrvutiasetsevad postid võrdsete kaugustega, \nmis ei ületa etteantud maksimaalkaugust. Liin algab ja lõpeb postiga.")
liini_pikkus = int(input("\nSiseestage liini pikkus täisarvuna meetrites\n"))
postide_max_kaugus = int(input("\nSiseestage postide vaheline maksimaalne kaugus samal kujul\n"))
#print(liini_pikkus, postide_max_kaugus)
ans = liini_pikkus // postide_max_kaugus
jääk = liini_pikkus % postide_max_kaugus
if jääk > 0:
    ans = ans + 1
ans = ans + 1
if ans < 2:
    ans = ans + 1
print(ans)