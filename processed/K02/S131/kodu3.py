# Funktsioonid teevad koodi rohkem loetavaks.
# Siin on ühe realine return funktsioon mis pole alati kõige parem idee, kune üks pikk rida pole kergesti aru saadav
# ja võib teha koodi lugemise raskemaks. Ma lihtsalt lazy tho
def create_username(first_name : str, second_name : str):
    return '{}.{}'.format(first_name.lower(), second_name.lower()).replace('ä','a').replace('ö','o').replace('õ','o').replace('ü','u')

# Main loop
# Try/except blocki pole vaja kuna siin ei saa olla vigast sisendit.
f_name = input('Sisesta eesnimi: ')
l_name = input('Sisesta perenimi: ')
print(create_username(f_name, l_name))

# Wait for input before closing
# Nagu alati
# Automaatkontrollile ei meeldi teine input
#input()
