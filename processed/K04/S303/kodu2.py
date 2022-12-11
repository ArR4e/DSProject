def summa(velocity1, velocity2):
    speed_of_light = 299792.458
    return (velocity1 + velocity2) / (1 + velocity1 * velocity2 / speed_of_light**2)

velocity1 = float(input('Velocity of the first body relative to the observer: '))
velocity2 = float(input('Velocity of the second body relative to the first body: '))
velocity3 = float(input('Velocity of the third body relative to the second body: '))
velocity4 = float(input('Velocity of the fourth body relative to the third body: '))

velocity_sum = summa(velocity1, velocity2)
velocity_sum = summa(velocity_sum, velocity3)
velocity_sum = summa(velocity_sum, velocity4)

print(f'Velocity sum is {velocity_sum} km/s')
