f=open('aadressid.txt ')

global tühi
tühi=[]
def kasutajanimed(rida):
    if 'http://www.ut.ee/~' in rida:
        osad=rida.split('/')
        tühi.append(osad[-2])
for i in f:
    i=i.strip()
    kasutajanimed(i)
  