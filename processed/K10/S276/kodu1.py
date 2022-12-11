def erinevad_sümbolid(tekst):
    return set(tekst)

def sümbolite_sagedus(tekst):
    sümbolid=set(tekst)
    sõnastik = {}
    for element in sümbolid:
        sõnastik[element]=tekst.count(element)
    return sõnastik

def grupeeri(tekst):
    sümbolid=set(tekst)
    täishäälikud=("aeiouõäöü")
    kaashäälikud=("kptgbdfhsšzžjlmnrv")
    sõnastik = {}
    for element in sümbolid:
        if element in täishäälikud:
            sõnastik["Täishäälikud"] = (element, tekst.count(element))
        elif element in kaashäälikud:
            sõnastik["Kaashäälikud"] = (element, tekst.count(element))
        else:
            sõnastik["Muud"] = (element, tekst.count(element))
    return sõnastik