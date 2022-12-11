def parool_kontroll(c,t):
    if len(c) < 8:
        return False
    if any(i.isdigit() for i in c) == False:
        return False
    if any(i.isalpha() for i in c) == False:
        return False
    for x in range(0, len(c)):
        if c[x] != t[x]:
            return False
    return True

login = input()
pass1 = input()
pass2 = input()
pass3 = ""

while True:
    if parool_kontroll(pass1, pass2) == True:
        for i in pass1:
            pass3 = i + pass3
        f = open("users.txt", "w")
        f.write(login + ":" + pass3)
        f.close()
        break
    pass1 = input()
    pass2 = input()