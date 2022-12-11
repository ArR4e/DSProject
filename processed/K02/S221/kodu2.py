pikkus = float(input('Kui pikk tuleb teie elektriliin!(meeter)'))
vahemaa = float(input('Mis on järjestikkuste postide maksimaalne vahemaa(meeter)?'))

postid = (pikkus/vahemaa)
postid = round(postid + 0.5) + 1

postid = str(postid)
print('Teil läheb vaja minimaalselt ' + postid +' posti')
