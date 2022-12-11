kiirus=0
c=299792.458
def summa(u,v):
    kiirus=(u+v)/((1+(u*v)/(c*c)))
    return kiirus
            
    
a=float(input("Sisestage esimene kiirus:"))
b=float(input("Sisestage teine kiirus:"))
d=float(input("Sisestage kolmas kiirus:"))
e=float(input("Sisestage neljas kiirus:"))
esimene=summa(a,b)
teine=summa(esimene,d)
kolmas=summa(teine,e)
print("Kiiruste summa on",float(esimene)+float(teine)+float(kolmas))