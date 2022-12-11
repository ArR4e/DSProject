sõnastik={}
fail1=open("lapsed.txt")
for rida in fail1:
    osad=rida.strip().split(" ")
    vanem=osad[0]
    laps=osad[1]
fail1.close()
abisõnastik={}
fail2=open("nimed.txt")
for rida in fail2:
    osad=rida.strip().split(" ")
    isikukood=osad[0]
    nimi=osad[1]+" "+osad[2]
    abisõnastik[isikukood]=nimi
fail2.close()
def seosta_lapsed_ja_vanemad(fail1, fail2):
    if isikukood ==laps:
        lapsenimi= abisõnastik[isikukood]
        if lapsenimi not in sõnastik:
            sõnastik[lapsenimi]=set()
    if isikukood ==vanem:
        vanemanimi=abisõnastik[isikukood]
            
        
    return sõnastik
sõnastik = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')
print(sõnastik)