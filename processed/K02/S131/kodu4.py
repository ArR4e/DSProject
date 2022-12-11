file_1_name = input('Sisesta sisend faili nimi: ')
file_2_name = input('Sisesta väljund faili nimi: ')



# "with" lubab avada mitut faili korraga, ilma et peaks hiljem kasutama "file.close()" mis võib meelest minna.
# kui with block saab läbi on failid automaatselt suletud.
with open(file_1_name) as eng, open(file_2_name, 'w') as est:
    # for loop lihtsalt võtab ühest failist rea ja paneb selle teisse, samal ajal replaceb "Hello" "Tere"ga
    count = 0
    for line in eng.readlines():
        count += line.count('Hello')
        est.write(line.replace('Hello', 'Tere'))
        
print(count)