from statistics import harmonic_mean
import matplotlib

with open('aktsiad.txt') as f:
    lines = f.readlines()
    inital_data = [entry.split(', ')[1].strip() for entry in lines]

print(inital_data)

def silu_andmed(lst, n):
    output = []
    for i in range(len(lst)):
        lower_index = max(0, i+1-n)
        num_list = lst[lower_index:i+1]
        har_mean = harmonic_mean(num_list)
        output.append(har_mean)

    return output
