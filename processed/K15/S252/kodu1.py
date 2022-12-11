import re

# . - suvaline sümbol
# ^ - teksti algus
# $ - teksti lõpp
# ? - 0 või 1 korda eelnevat
# * - 0 kuni lõpmatus eelneva korduseid
# + - 1 kuni lõpmatus eelneva korduseid
# {x} - eelneva kordus x korda
# {x, y} - eelneva kordus x kuni y korda
# [] - tähemärkide kogumik/vahemikud
# () - grupid


fail = open("aadressid.txt")
for read in fail:
    read = fail.readlines()
    #rida = read.split("\n")
    #punkt = re.search("[.]",read)
    #otsing = re.search("^w/$",read)
    nimed = re.search("^~(.+) /$",read)
    
    


print(nimed.group(1))
#print(nimed)
fail.close()