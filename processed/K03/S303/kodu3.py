natural_number = int(input('Enter a natural number: '))
num_sum = 0
square_sum = 0

for i in range(1, natural_number+1):
    num_sum += i
    square_sum += i**2
    
print(num_sum**2 - square_sum)
