


def seosta_lapsed_ja_vanemad(lastefailinimi, nimedefailinimi):
    ik_d = {}
    lastefailinimi = open('lapsed.txt')
    for rida in lastefailinimi:
        kood = rida.strip().split()
        ik_d[kood[0]] = kood[1]
    lastefailinimi.close()
    nim_d = {}
    nimedefailinimi = open('nimed.txt', encoding = 'UTF-8')
    for rida in nimedefailinimi:
        kood = rida.strip().split(" ", 1)
        nim_d[kood[0]] = kood[1]
    nimedefailinimi.close()
    print(ik_d, nim_d)

print(seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt'))


