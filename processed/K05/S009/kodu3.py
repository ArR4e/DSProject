def moos(suur, väike, kogus):
    marju_keedetud = 0
    kasutatud_karpe = 0
    
    while kogus < 0:
        if suur >= 0:
            kogus -= 5
            marju_keedetud += 5
            suur -= 1
            kasutatud_karpe += 1
            print(int(kasutatud_karpe))
        
        elif suur == 0:
            kogus -= 1
            marju_keedetud += 1
            väike -= 1
            kasutatud_karpe += 1
        print(int(kasutatud_karpe))
        
        elif kogus > 0:
            print(-1)
    
        
print(moos(5, 1, 15))
        
        
        