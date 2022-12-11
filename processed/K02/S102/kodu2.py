l=int(input('Palun sisesta taisarvuna liini kogupikkus: '))
a=int(input('Palun sisesta taisarvuna kahe posti vaheline maksimaalne kaugus: '))
b=l%a
if b==0:
    b=int(l/a)+1
    print('Minimaalne vajalik postide hulk on ', b)
else:
    b=int(l/a)+2
    print('Minimaalne vajalik postide hulk on ', b)