income = float(input('Enter your annual income: '))

if income <= 6000:
    tax_free = income
elif income > 6000 and income <= 14400:
    tax_free = 6000
elif income > 14400 and income <= 25200:
    tax_free = 6000 - 6000 / 10800 * (income - 14400)
elif income > 25200:
    tax_free = 0
else:
    print("You've entered invalid number")
    exit()
    
print(f'Your tax free income is {round(tax_free, 2)}')
