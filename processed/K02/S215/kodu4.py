def replace_with_phrase(lines, replacable, phrase):
    total_replaced = 0
    for line in lines:
        total += line.count(replacable)
        line.replace(replacable, phrase)
    return lines, total_replaced



file_1 = input("File 1: ")
file_2 = input("File 2: ")

with open(file_1, "r", encoding="utf-8") as file:
    new_lines, replaced = replace_with_phrase(
        file.readlines(), "Hello", "Tere"
    )
with open(file_2, "w", encoding="utf-8") as file:
    file.writelines(new_lines)

print(replaced)    
