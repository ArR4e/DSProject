from turtle import *

def ruut_fraktal(ruut, pikkus, nurk):
    for i in range(3): #3, sest ta joonistab 3 nurka fraktaleid(kui joonistab)
        
        fd(pikkus) #sellega liigub otse kuni tasemed otsa saavad ja siis hakatakse otsast ruute joonistama
        
        if ruut > 1: #kui on vaja nurkadesse fraktaleid joonistada, siis viib igasse nurka ühe fraktali astme võrra sügavamale
            
            pikkus = pikkus/2 #iga tase poole võrra lühem
            
            nurk = -nurk #iga tase sügavamale vajab vastaspoolset esimest pööret
            
            ruut_fraktal(ruut - 1,pikkus,nurk) #rekursioon
            
            nurk = -nurk #teisele poole pööre, et ikka ruut tekiks
            
            pikkus *= 2 #tagasi tulles, et algne ruudu külje pikkus tagasi saada

        right(nurk) #keerab veel ühe korra, et õige suund saada
        
    forward(pikkus) #viib algsesse positsiooni ning keerab õige suuna
    right(nurk)


speed(300)
ruut_fraktal(5,100,90)
