#sain abi konsultatsioonist ja murelahendajalt
teepikkus = float(input("Mis on sinu teepikkus(kilomeetrites)? "))
fail = open("taksohinnad.txt", encoding = "UTF-8")
kõige_odavam = 0
for rida in fail:
    järjend = rida.rstrip().split(",")
    #hind = stardihind + (teepikkus * kilomeetri_hind)
    # stardihind ehk järjend[1]; kilomeetri_hind ehk järjend[2]
    hind = float(järjend[1]) + (teepikkus * float(järjend[2]))
    if hind < kõige_odavam or kõige_odavam == 0:
        kõige_odavam = hind
        odavaim_takso = järjend

fail.close()
print("Kõige odavam takso on " + odavaim_takso[0] +".")