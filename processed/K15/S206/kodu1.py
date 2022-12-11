import re
print("Kasutajanimed on: ")
with open("aadressid.txt", encoding="UTF-8") as f:
    for rida in f:
        if re.match(' *.{7,8}w{3}\\.ut\\.e{2}/~', rida):
            tilde = rida.index('~')
            print(rida[tilde+1:tilde+rida[tilde:].index('/')])
    