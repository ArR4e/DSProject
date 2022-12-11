import re
print('Kasutajanimed on:')
with open('aadressid.txt','r' , encoding = 'utf-8') as f:
    for aadress in f:
        #Kui ma jätan '^' märgi ära, siis kaob üks, error ära, aga teine tekib... ma ei oska selle taandega aadressi ees midagi peale hakata 
        nimed = re.search('^http://www.ut.ee/~([a-z, 0-9]+)/{1}', aadress)
        if nimed:
            print(nimed.group(1))
    