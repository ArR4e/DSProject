import re

f = open("aadressid.txt", encoding="UTF-8")
lines = f.readlines()
print("Kasutajanimed on:")
for line in lines:
    vastus=re.search("(?<=\.ee/~)(.*?)(?=\/)", line)
    if vastus:
        print(vastus.group())
        
#https://stackoverflow.com/questions/1454913/regular-expression-to-find-a-string-included-between-two-characters-while-exclud