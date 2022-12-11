from math import ceil
liin = int(input("kui pikk on liin meetrites?  "))
vahemaa = int(input("kui suur on postide vahemaa meetrites?  "))

postid = ceil(liin/vahemaa+1)
print(postid)