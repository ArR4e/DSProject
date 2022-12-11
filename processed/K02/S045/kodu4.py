with open(input('Vali sisend'), 'r') as f: #https://stackoverflow.com/questions/3142054/python-add-items-from-txt-file-into-a-list
    tekst = f.readlines()
    
hello_count = 0
with open(input('Vali väljund'), 'w') as f:
    for i in tekst:
        hello_count += i.count('Hello')
        i = i.replace('Hello', 'Tere')
        f.write(i)
print(f'Tehti {hello_count} asendamist.')