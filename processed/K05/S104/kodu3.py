s_karbid = int(input('Suurte karpide arv: '))
v_karbid = int(input('Väikeste karpide arv: '))
moosi_kogus = int(input('Moosi kogus: '))
kasutatud = 0

def moos(s_karbid, v_karbid, moosi_kogus):
    while moosi_kogus >= 5:
        moosi_kogus -= 5
        s_karbid -= 1
        kasutatud += 1
    else v_karbid -= 1
    if v_karbid = 0:
        break

moos(s_karbid, v_karbid, moosi_kogus)
print('Kasutatud karpe on: ', kasutatud)