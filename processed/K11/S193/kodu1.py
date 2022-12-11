fail_lapsed = open("lapsed.txt", 'r', encoding = "UTF-8")
fail_nimed = open("lapsed.txt", 'r', encoding = "UTF-8")


def seosta_lapsed_ja_vanemad(fail_lapsed, fail_nimed):
    sõnastik = {}
    for rida in fail_lapsed:
        rida = rida.strip()
        isikukood_v = rida[1]
        isikukood_l = rida[0]
        
        
        
fail_lapsed.close()
fail_nimed.close()