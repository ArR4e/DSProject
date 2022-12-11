import re

fail = open("aadressid.txt")

print("Kasutajanimed on:")
for rida in fail:
    if rida == "":
        break
    elif re.search("http://www.*", rida):
        if re.search("~[a-yõäöü]", rida):
            järjend = rida.strip().split("/")
            for element in järjend:
                if re.match("~", element):
                    print(element[1:])
    else:
        continue

fail.close()