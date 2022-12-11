import re

print('Kasutajanimed on:')

with open('aadressid.txt', 'r', encoding='UTF-8') as fail:
    for rida in fail:
        if bool(re.match('http[:][/][/]www[.]ut[.]ee[/][~]', rida.strip())):
            print(rida[rida.find('~') + 1 : rida[rida.find('~')+1:].find('/') + rida.find('~') + 1 ])
            