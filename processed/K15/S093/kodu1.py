import re

fail = open('aadressid.txt', 'r', encoding = 'UTF-8')

for line in fail.readlines():
    result = re.search('www\.ut\.ee/~(.*?)/.*', line)
    if result != None:
        print(result.group(1))
    

    

    