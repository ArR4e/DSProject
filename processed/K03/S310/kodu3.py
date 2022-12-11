# automaatne kontroll kahjuks ei töötanud - annab errorit:
# You are using an encrypted connection.
# To use an encrypted connection with the execution servers it is required you accept its certificates.
# If you have problems with this process, you can try to use a http (unencrypted) connection or other browser.
# Please, click on the following links (server #) and accept the offered certificate.
# Server 10

n = int(input('Sisesta siia naturaalarv: '))

i = 0
naturaalarvu_ruutude_summa = 0
naturaalarvu_summa = 0


while i < n:
    naturaalarvu_ruutude_summa = naturaalarvu_ruutude_summa + (n * n)
    naturaalarvu_summa = naturaalarvu_summa + (n)

    n = n - 1
    

naturaalarvu_summa_ruut = naturaalarvu_summa * naturaalarvu_summa

print(naturaalarvu_summa_ruut - naturaalarvu_ruutude_summa)




