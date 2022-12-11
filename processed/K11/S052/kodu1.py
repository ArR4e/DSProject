def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
    f = open(lastefail, "r")
    nimekiri = {}
    for rida in f:
        
        vanem = rida.split(" ",1)[0]
        laps = rida.split(" ",1)[1].strip()
        
        if rida.split(" ")[0] in nimekiri:
            nimekiri[vanem] = nimekiri[vanem] + " " + (laps)
        else:  
            nimekiri[vanem] = laps
    f.close()
    
    print(nimekiri)

seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

# Siin all on kommentaarina minu üritused muuta isikukoode nimedeks, kuid ei saanud lõpuni hakkama.

# def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
#     f = open(lastefail, "r")
#     nimekiri = {}
#     for rida in f:
#         
#         vanem = rida.split(" ",1)[0]
#         laps = rida.split(" ",1)[1].strip()
#         
#         if rida.split(" ")[0] in nimekiri:
#             with open(nimedefail, "r") as f1:
#                 for rida in f1:
#                     ik = rida.split(" ",1)[0]
#                     nimed = rida.split(" ",1)[1].strip()
#                     
#                 nimekiri[nimed[ik.index(vanem)]] = nimekiri[vanem] + " " + (laps)
#         else:
#             with open(nimedefail, "r") as f1:
#                 for rida in f1:
#                     ik = rida.split(" ",1)[0]
#                     nimed = rida.split(" ",1)[1].strip()
#                 nimekiri[nimed[ik.index(vanem)]] = laps
#     f.close()
#     
#     print(nimekiri)
    
#     f = open(nimedefail, "r")
#     for rida in f:
#         
#         ik = rida.split(" ",1)[0]
#         nimi = rida.split(" ",1)[1].strip()
#         nimekiri[ik] = nimekiri[nimi]
#         del nimekiri[ik]
# #         if len(nimekiri[vanem]) == 2:
# #             nimekiri.update({vanem:
#       #  nimekiri.update({vanem:laps})
#         #nimekiri[ik] = nimekiri.pop(vanem)
#     print(nimekiri)
#     f.close()
    
