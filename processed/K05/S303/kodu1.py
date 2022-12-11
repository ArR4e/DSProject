from string import digits, ascii_letters
name = input('Enter your name: ')

while True:
    password = input('Enter a password: ')
    
    if password != input('Repeat password: '):
        print("Passwords don't match")
        continue
    
    if len(password) < 8:
        print("Password must contain at least 8 symbols")
        continue
    
    digits_present = False
    letters_present = False
    for symbol in password:
        if symbol in digits:
            digits_present = True
        if symbol in ascii_letters:
            letters_present = True
    
    if not digits_present or not letters_present:
        print("Password must contain at least 1 digit and 1 letter")
        continue
        
    break

password = password[::-1]

with open('users.txt', 'a') as f:
    f.write(f'{name}:{password}\n')
