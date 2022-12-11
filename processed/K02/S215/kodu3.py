def name_to_username(first_name, last_name):
    return f"{first_name.lower()}.{last_name.lower()}"


first_name = input("Sisestage eesnimi: ")
last_name = input("Sisestage perenimikod: ")
print(name_to_username(first_name, last_name))
