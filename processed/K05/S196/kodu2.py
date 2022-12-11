import string

sümbolid = string.punctuation #!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
sümbolite_järjend = list(sümbolid)

def pööra_tagurpidi(sõna):
    sõna_pikkus = len(sõna) - 1 #sest algab 0st
    uus_sõna = ""
    while sõna_pikkus >= 0:
        täht = sõna[sõna_pikkus]#või number
        uus_sõna = uus_sõna + täht
        sõna_pikkus -= 1
    return uus_sõna

sümbolid_tagurpidi = pööra_tagurpidi(sümbolid)
tagurpidi_sümbolite_järjend = list(sümbolid_tagurpidi)
#panen iagle sümbolile vastama tagurpidises sümbolite järjendis samal kohal asuva sümboli

def suurväike(sõne):
    uus_sõne = ""
    sõne_pikkus = len(sõne) - 1#indeksid algavad 0ga
    i = 0
    while i <= sõne_pikkus:
        element = sõne[i] 
        if element.isdigit() == True:#kas on number, siis ei muutu
            uus_sõne += element
        elif element.islower() == True:#kas on väiketäht
            uus_element = element.upper()
            uus_sõne += uus_element
        elif element.isupper() == True:
            uus_element = element.lower()
            uus_sõne += uus_element
        elif sümbolite_järjend.count(element) == 0:#kas on tühik
            uus_sõne += " "
        else:#ei ole ka tühik, seega sümbol
            jrk = sümbolite_järjend.index(element)
            vastav_sümbol = tagurpidi_sümbolite_järjend[jrk]
            uus_sõne += vastav_sümbol
        i += 1
    return uus_sõne

print(suurväike("MinA oleN Tubli!!"))