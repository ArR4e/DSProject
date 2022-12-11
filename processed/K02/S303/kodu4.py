read_file_name = input('Where read from: ')
write_file_name = input('Where write to: ')

with open(read_file_name, 'r') as read_file, open(write_file_name, 'w') as write_file:
    buffer = read_file.read()
    write_file.write(buffer.replace('Hello', 'Tere'))
    print(f'Total replacements: {buffer.count("Hello")}')
