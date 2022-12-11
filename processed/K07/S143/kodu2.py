with open("taksohinnad.txt", "r", encoding="UTF-8") as f:
    try:
        print(f"Kõige odavam takso on {(lambda b: ((lambda c: b[c.index(min(c))].split(',')[0])((lambda x:([(float(y[1])+x*float(y[2])) for y in [x.strip().split(',') for x in b]]))(float(input('Sisesta tee pikkus kilomeetrites: '))))))(f.readlines())}.")
    except:
        print(f"Kõige odavam takso on ")