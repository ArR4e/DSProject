def väljasta_liin(eel,järg,s):
    if järg not in s:
        return False
    if s[järg][0]==eel or s[järg][1]==eel:
        print(eel)
        print(järg)
        return True
    if väljasta_liin(eel,s[järg][0],s):
        print(järg)
        return True
    if väljasta_liin(eel,s[järg][1],s):
        print(järg)
        return True
    return False