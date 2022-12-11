salary_text = input('Sisestage aastatulu: ')
salary = float(salary_text)
taxfree=0

if salary <= 6000:
               taxfree=salary
               
elif salary > 6000 and salary <= 14000:
               taxfree=6000
        
elif salary <= 25200 and salary >=14400:
               taxfree=6000-6000/10800*(salary-14400)

else:
               taxfree=0
              
print("Maksuvaba tulu on " + str(round(taxfree,2)))            
