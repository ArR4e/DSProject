def erinevad_sümbolid(x):
    x=set(x)
    return x

def sümbolite_sagedus(y):
    sõnastik={}
    for i in y:
        if i not in sõnastik:
            sõnastik.update({i : 1})
        elif i in sõnastik:
            sõnastik[i]+=1
    return sõnastik

def grupeeri(z):
    täishäälikud=('a', 'e', 'i', 'o', 'u', 'õ', 'ä', 'ö', 'ü')
    kaashäälikud=('b', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'š', 'z', 'ž' , 't', 'v')
    sõnastik={'Täishäälikud':{}, 'Kaashäälikud':{}, 'Muud':{}}
    for i in z:
        if i in täishäälikud:
            if i not in sõnastik['Täishäälikud']:
                sõnastik['Täishäälikud'][i]=1
            elif i in sõnastik['Täishäälikud']:
                sõnastik['Täishäälikud'][i]+=1
        elif i in kaashäälikud:
            if i not in sõnastik['Kaashäälikud']:
                sõnastik['Kaashäälikud'][i]=1
            elif i in sõnastik['Kaashäälikud']:
                sõnastik['Kaashäälikud'][i]+=1
        elif i not in (täishäälikud or kaashäälikud):
            if i not in sõnastik['Muud']:
                sõnastik['Muud'][i]=1
            elif i in sõnastik['Muud']:
                sõnastik['Muud'][i]+=1
    return sõnastik
    

#https://www.kite.com/python/answers/how-to-increment-a-value-in-a-dictionary-in-python
#https://careerkarma.com/blog/python-add-to-dictionary/    