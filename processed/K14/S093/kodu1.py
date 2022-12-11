def rek_abs(järjend):
    järjend_copy = järjend.copy()
    for index, elem in enumerate(järjend_copy):
        if isinstance(elem, list):
            järjend_copy[index] = rek_abs(elem)
        else:
            järjend_copy[index] = abs(elem)
    return järjend_copy
    
järjend = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
j = rek_abs(järjend)           
print(j)
