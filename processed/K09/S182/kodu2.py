from random import randint
def minu_shuffle(järjend):
    if len(järjend)<2:
        return
    for curr_idx, curr_val in enumerate(järjend):
        swap_idx= randint(curr_idx, len(järjend)-1)
        swap_val=järjend[swap_idx]
        
        if swap_idx !=curr_idx:
            järjend[curr_idx], järjend[swap_idx]=swap_val, curr_val
järjend=[1, 2, 3, 4, 5, 6]
minu_shuffle(järjend)
print(järjend)