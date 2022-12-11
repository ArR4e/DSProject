first_name = input('Sisestage eesnimi: ').lower()
last_name = input('Sisestage perenimi: ').lower()

username = first_name + '.' + last_name

corrected_username = ''
for letter in username:
    if letter == 'ö' or letter == 'õ':
        corrected_username += 'o'
    elif letter == 'ü':
        corrected_username += 'u'
    elif letter == 'ä':
        corrected_username += 'a'
    else:
        corrected_username += letter
 
print(corrected_username)
