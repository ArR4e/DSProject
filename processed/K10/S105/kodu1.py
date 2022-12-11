def erinevad_sümbolid(a):
    elemendid=set()
    for ele in a:
        if ele in elemendid:
            continue
        else:
            elemendid.add(ele)
    return elemendid

def sümbolite_sagedus(a):
    elemendid={}
    for ele in a:
        if ele in elemendid:
            elemendid[ele]+=1
        else:
            elemendid[ele]=1
    return elemendid

def grupeeri(a):
    elemendid={}
    th="iüueöõoäaAEIOUÜÕÖÄ"
    kh="BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsŠšZzŽžTtVvWwXxYy"
    khd=[]
    thd=[]
    muu=[]
    for ele in a:
        if ele in kh:
            khd.append(ele)
        elif ele in th:
            thd.append(ele)
        else:
            muu.append(ele)
    khds=sümbolite_sagedus(khd)
    thds=sümbolite_sagedus(thd)
    muuds=sümbolite_sagedus(muu)
    khd1=set()
    thd1=set()
    muu1=set()
    for ele in khd:
        khd1.add((ele, khds[ele]))
    for ele in thd:
        thd1.add((ele, thds[ele]))
    for ele in muu:
        muu1.add((ele, muuds[ele]))
    elemendid["Täishäälikud"]=thd1
    elemendid["Kaashäälikud"]=khd1
    elemendid["Muud"]=muu1   
    return elemendid
grupeeri("sõida tasa üle silla")