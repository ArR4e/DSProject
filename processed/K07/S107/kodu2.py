
tee_pikkus = input("Sisesta tee pikkus kilomeetrites: ")
sisseistumise_hind = []
kilomeetri_hind = []

f = open("taksohinnad.txt", r, encoding="UTF-8")
def taksohind(järjend):

    for rida in f:
        järjend = f.readline().split(",")
        nimed = järjend[0]
        sisseistumise_hind = järjend[1]
        kilomeetri_hind = järjend[2]
        hind = sisseistumise_hind + int(tee_pikkus)*kilomeetri_hind
        

f.close()

print("Kõige odavam on " + )

    