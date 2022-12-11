kaugus = float(input('Sisesta tee pikkus kilomeetrites: '))
fail = open('taksohinnad.txt')
hind = []
nimed = []
for line in fail:
    jarjend = line.strip('\n').split(',')
    nimed += [jarjend[0]]
    try:
        a = float(jarjend[1])
        b = float(jarjend[2])
    except:
        continue
    raha = kaugus*b+a
    hind += [raha]
    
if hind[0] < hind[1] and hind[0] < hind[2]:
    print('Kõige odavam takso on ', nimed[0])
elif hind[1] < hind[0] and hind[1] < hind[2]:
    print('Kõige odavam takso on ', nimed[1])
else:
    print('Kõige odavam takso on ', nimed[2])
    