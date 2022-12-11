def transponeeriK(m):
    päästerõngas = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    maatriks = []
    for rida2 in päästerõngas:
        tagurpidi = rida2[::-1]
        maatriks.append(tagurpidi) 
    tagurpidi_maatriks = []    
    for rida3 in maatriks[::-1]:
        tagurpidi_maatriks.append(rida3)
        
    return tagurpidi_maatriks
        

print(transponeeriK([[1, 2], [3, 4]]))
        
        
