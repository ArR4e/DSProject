taksohinnad=open('taksohinnad.txt')

tee_pikkus=float(input('Kui pikk on kodutee? Sisesta tee pikkus kilomeetrites: '))
istumise_hind=0
km_hind=0
hind_kokku=10**10000
parim_takso=''

for rida in taksohinnad:  
    
    if rida=='':
        break
    
    rida=rida.split(',')
    praegu_parim_takso=rida[0]
    istumise_hind=float(rida[1])
    km_hind=float(rida[2])
    praegune_hind=istumise_hind+km_hind*tee_pikkus
    
    if praegune_hind<hind_kokku:
        hind_kokku=praegune_hind
        parim_takso=praegu_parim_takso

print(parim_takso)
    
    

taksohinnad.close()