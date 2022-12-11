def poisse_ja_tüdrukuid(järjend):
    poisid = 0
    tüdrukud = 0
    i = 0
    for el in j:
        if el[-1] == "P":
            poisid += 1
        elif el[-1] == "T":
             tüdrukud += 1
    print(poisid, tüdrukud)
        
        
j = ["Martin P", "Paula T", "Joosep P", "Artur P", "Marta-Mia T", "Ingemari T", "Harry P", "Siim P"]
poisse_ja_tüdrukuid(j)