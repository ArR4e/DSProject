import string, random
def suurväike(sõne):
    # defineeri suured ja väikesed tähed ning kirjavahemärgid
    suurtähed = "ABCDEFGHIJKLMNOPQRSŠZŽTUVWÕÄÖÜXY"
    väiketähed = "abcdefghijklmnopqrsšzžtuvwõäöüxy"
    kirjavahemärgid = string.punctuation
    # leia juhuslik märk, millega teised kirjavahemärgid asendada
    asendusmärk = kirjavahemärgid[random.randint(0, len(kirjavahemärgid) - 1)]
    # alusta uue sõne konstrueerimist
    uus = ""
    for i in range(len(sõne)):
        # salvesta praegune pikkus
        # juhul kui see ei muutu tsüklite sees, siis tavaliselt
        # on tegemist tühikuga (mis tähendab, et uuele sõnele lisatakse
        # sama tähemärk)
        vanapikkus = len(uus)
        # kontrolli, kas tegemist on suure tähega
        # kui jah, siis lisa väiketäht uude sõnesse ning lõpeta tsükkel
        for j in range(len(suurtähed)):
            if suurtähed[j] == sõne[i]:
                uus += väiketähed[j]
                break
        # kontrolli, kas tegemist on väikese tähega
        # kui jah, siis lisa suurtäht uude sõnesse ning lõpeta tsükkel
        for j in range(len(väiketähed)):
            if väiketähed[j] == sõne[i]:
                uus += suurtähed[j]
                break
        # kontrolli, kas tegemist on kirjavahemärgiga
        # kui jah, siis lisa muutuja 'asendusmärk' uude sõnesse ja lõpeta tsükkel
        for j in range(len(kirjavahemärgid)):
            if kirjavahemärgid[j] == sõne[i]:
                uus += asendusmärk
                break
        # lisa sama tähemärk, kui sõne pikkus ei muutunud
        if vanapikkus == len(uus):
            uus += sõne[i]
    # tagasta uus sõne
    return uus
