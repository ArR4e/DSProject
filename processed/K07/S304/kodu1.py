def poisse_ja_tüdrukuid(järj):
    n = 0
    m = 0
    
    for line in järj:
        järj = line.split()
        sugu = järj[-1]

        if sugu == 'T':
            n += 1
            
        if sugu == 'P':
            m += 1

    return (abs(m), abs(n))
 
järj = ['Mari T', 'Liisa T', 'Karl Gustav P', 'Stiina T', 'Mati P' ]
poisse_ja_tüdrukuid(järj)
e = (poisse_ja_tüdrukuid(järj))
print(e) 

         