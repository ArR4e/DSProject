inp = input("Sisendfail")
out = input("Väljundfail")

with open(inp, "r") as f_in:
    with open(out, "w") as f_out:
        f_data = f_in.read()
        changes = f_data.count("Hello")
        f_data = f_data.replace("Hello", "Tere")
        f_out.write(f_data)
        print(changes)