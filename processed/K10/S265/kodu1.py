def erinevad_sümbolid(text):
    x = set()
    for i in text:
        if i not in x:
            x.add(i)
    return x

def sümbolite_sagedus(text):
    x = {}
    for i in text:
        if i not in x:
            x[i] = 1
        else:
            x[i] += 1
    return x

def grupeeri(text):
    final = {}
    final['Täishäälikud'] = set()
    final['Kaashäälikud'] = set()
    final['Muud'] = set()
    x = sümbolite_sagedus(text)
    for i in x:
        if i.isalpha():
            if i in ('a','e','i','o','u','õ','ä','ö','ü','A','E','I','O','U','Õ','Ä','Ö','Ü'):
                final.get('Täishäälikud').add((i, x.get(i)))
            else:
                final.get('Kaashäälikud').add((i, x.get(i)))
        else:
            final.get('Muud').add((i, x.get(i)))
    return final

print(grupeeri("sõida tasa üle silla"))