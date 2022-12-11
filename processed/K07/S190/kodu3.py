#mul on vaja, et ta tükeldaks isikukoodi õigetest kohtadest
# ja siis ma saan nende tükkidega edasi toimetada
def sünnikuupäev(isikukood):
    sajandi_kood = isikukood[0]
    aasta = isikukood[1:3]
    kuu_nr = isikukood[3:5]
    päev = isikukood[5:7]
    
    if sajandi_kood in ["1","2"]:
        aasta_arv = "18"+aasta
    elif sajandi_kood in ["3","4"]:
        aasta_arv = "19"+aasta
    else:
        aasta_arv = "20"+aasta
        
    kuude_järjend = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu = kuude_järjend[int(kuu_nr)-1]
    
    return päev+". "+kuu+" "+aasta_arv
