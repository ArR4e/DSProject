import re

fail = open("aadress.txt", encoding="UTF-8")

for rida in fail:
    regex = re.search(r"ut\.ee\/~(.+?)\/", rida)
    if regex:
        print(regex.group(1))
                
