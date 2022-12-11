import re
fail = open('aadressid.txt')


for rida in fail:
    kasutajanime_regex = r'^https://www.ut.ee/([A-Za-z]$)'
    
    if re.search(kasutajanime_regex, rida):
        re.search(r'^https://www.ut.ee/([A-Za-z]$)', rida)
        print(re.search(kasutajanime_regex))
    else:
        continue