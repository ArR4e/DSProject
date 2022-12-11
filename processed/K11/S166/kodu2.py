def transponeeriK(maatriks):
    m_read=len(maatriks)
    m_veerud=len(maatriks[0])
    trans_maatriks=[]
    i=0
    for veerg in maatriks[0]:
        t_rida=[]
        for rida in maatriks:
            t_rida.append(rida[-i])
        t_rida.reverse()
        trans_maatriks.append(t_rida)
        i+=1
    trans_maatriks.append(trans_maatriks.pop(0))
    return trans_maatriks