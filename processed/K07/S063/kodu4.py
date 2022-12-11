###############################################################################################################
## Kirjuta programm, mis kilpkonna abil näitab võimalikult suurt osa värvidest                                #
## aadressilt http://wiki.tcl.tk/16166, näiteks värvid antud loetelu keskosast,                               #
## kus pole mitmesõnalisi nimesid.                                                                            #
###############################################################################################################
import turtle

# salvestame värvide nimed faili, halli värve ei võta
f = open("turtle_palette.txt")
# hakkame paletti koostama
palett = ""
# loendame faili ridade kaupa
while True:
    rida = f.readline().strip()
    # kui on faili lõpp
    if rida == "":
        break
    # viskame kõike nimesid, mis on märkide '{' ja '}' vahel
    # kordame nii palju mitu sellist nimi reas on
    for i in range(rida.count("{")):
        if rida.find("{") != -1 and rida.find("}") != -1:
            rida = rida[:rida.find("{")] + rida[rida.find("}")+1:]
    # lisame paleti juurde
    palett += " "+rida.strip()
f.close()
# jaotame juppideks (värvinimed)
palett = palett.split()
f.close()

# hakkame kilpkonnaga joonistama
turtle.setup(800, 600)
turtle.speed(0)
turtle.delay(0)
# 360 on täisring, iga pöördenurk on 360 jagatud paletti värvide arvuga
pöördenurk = 360/len(palett)
# 
suund = 90
# ringi raadius
raadius = 150
# kilpkonna esialgne koht, võib muuta
punkt = (25 + raadius, 50)
ringi_punkt = (25, 50)
# hakkame joonistama segmendid iga värvi järgi
for värv in palett:
    # praegune värv
    turtle.color(värv, värv)
    # lähme esialgsele kohale, ei värvi praegu 
    turtle.penup()
    turtle.goto(punkt)
    # pöörame kilpkonna suunda
    turtle.setheading(suund)
    # hakkame segmenti värviga täitma
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(raadius, extent = pöördenurk)
    # nüüd lähme tagasi ja ei värvi, salvestame praegune koht
    suund = turtle.heading()
    punkt = turtle.position()
    turtle.penup()
    # tagasi ringi keskele
    turtle.goto(ringi_punkt)
    # segment on läbi värvitud
    turtle.end_fill()
turtle.exitonclick()
###############################################################################################################