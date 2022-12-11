import matplotlib.pyplot as plt
from statistics import harmonic_mean

def silu_andmed(_list, n):
    _return = []
    for i in _list:
        if  _list.index(i) == 0:
            _return.append(i)
        elif _list.index(i) < n:
            _return.append(harmonic_mean(_list[0:_list.index(i)+1]))
        elif _list.index(i) >= n:
            _return.append(harmonic_mean(_list[_list.index(i)-2:_list.index(i)+1]))
    return _return
a = [2, 1, 3, 4, 5]

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(a, silu_andmed(a, 3) )
ax.set_xlabel("Arvad") 

plt.show() 