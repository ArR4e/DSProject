sõne=input("")

def erinevad_sümbolid(sõne):
    hulk=set()
    for el in sõne:
        hulk.add(el)
    return hulk
    
erinevad_sümbolid(sõne)


def sümbolite_sagedus(sõne):
    sõnastik = {}
    f=[]
    for el in sõne:
        sõnastik[el]=0
        if el in sõne:
            f.append(el)
        
        
        if f.count(el)==1:  
            sõnastik[el]=sõnastik[el]+1
        n=f.count(el)
        if f.count(el)>1:
            sõnastik[el]+=n
            
            
       
                
                
    return sõnastik

sümbolite_sagedus(sõne)

def grupeeri(sõne):
    sõnastik = {}
    t="Täishäälikud:"
    k="Kaashäälikud:"
    m="Muud sümbolid:"
    #sõnastik[t] = set()
    #sõnastik[k] = set()
    #sõnastik[m] = set()
    f=[]
    for el in sõne:
        #sõnastik[t]=0
        #sõnastik[k]=0
        #sõnastik[m]=0
        
        if el.lower() in "aeiouõaöü":
            sõnastik[t] = {}
            
            for el in el:
                sõnastik[t, el]=0
                if el in sõne:
                    f.append(el)
        
        
                if f.count(el)==1:  
                    sõnastik[t, el]=sõnastik[t, el]+1
                n=f.count(el)
                if f.count(el)>1:
                    sõnastik[t, el]+=n
        if el.lower() in "bcdfghjklmnpqrstvwxšžyz":
            sõnastik[k] = {}
            
            for el in el:
                sõnastik[k, el]=0
                if el in sõne:
                    f.append(el)
        
        
                if f.count(el)==1:  
                    sõnastik[k, el]=sõnastik[k, el]+1
                n=f.count(el)
                if f.count(el)>1:
                    sõnastik[k, el]+=n
        if not (el.lower() in ("aeiouõaöü") or el.lower() in("bcdfghjklmnopqrstvwxšžyz")):
            sõnastik[m] = {}
            
            for el in el:
                sõnastik[m, el]=0
                if el in sõne:
                    f.append(el)
        
        
                if f.count(el)==1:  
                    sõnastik[m, el]=sõnastik[m, el]+1
                n=f.count(el)
                if f.count(el)>1:
                    sõnastik[m, el]+=n
                    
    return sõnastik
