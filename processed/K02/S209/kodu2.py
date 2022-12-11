import math

meetrid = int(input("Sisesta meetrite arv: "))
postid = int(input("postide maksimaalkaugus:"))

print("Nii:", math.ceil(meetrid / postid + 1))