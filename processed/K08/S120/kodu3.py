import film

def töötleKäsk(command, argument):
    if command.upper() == 'K':      
        output_list = film.loetleFilmid(argument)
        if output_list == []:
            print('Antud žanrit ei leitud.')
        else:
            print(output_list)
    elif command.upper() == 'L':
        arguments = argument.split(' ')
        film.lisaFilm(' '.join(arguments[1:]), arguments[0])
        print('Film lisatud!')
    elif command.upper() == 'V':
        film.kustutaFilm(argument)
        print('''Film nimekirjast kustutatud!\nHead vaatamist!''')
    else:
        return False
    return True

print('''=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===''')

command = True
while command:
    input_command = input('> ')
    split_input = input_command.split(' ')
    
    input_prefix = split_input[0]
    input_argument = ' '.join(split_input[1:])
    command = töötleKäsk(input_prefix, input_argument)
    if not command:
        break