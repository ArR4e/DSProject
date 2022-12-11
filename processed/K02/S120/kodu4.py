source_file = input('Lähtefaili nimi: ')
destination_file = input('Sihtfaili nimi: ')

with open(source_file, 'r') as s_f:
    source_text = s_f.read()
    word_count = source_text.count('Hello')
    
    with open(destination_file, 'w') as d_f:
        d_f.write(source_text.replace('Hello', 'Tere'))

print(f'Tehti {word_count} asendamist.')
