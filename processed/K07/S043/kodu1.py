jarjend = ['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T', 'Martti Kallas P']
def poisse_ja_tüdrukuid(järjend):
    po = 0
    ty = 0
    if len(järjend) !=0:
        for persoon in järjend:
            if persoon[-1] == 'P':
                po += 1
            else:
                ty += 1
        return (po, ty)
    else:
        return (0, 0)
    
print(poisse_ja_tüdrukuid(jarjend))