from statistics import harmonic_mean
import matplotlib.pyplot as plt

def silu_andmed(l,n):
    return [harmonic_mean(l[0:i+1]) if i<=n-1 else harmonic_mean(l[i-n+1:i+1]) for i in range(len(l))]
#print(silu_andmed([2, 1, 3, 4, 5], 3))
with open("aktsiad.txt","r",encoding="UTF-8") as f:
    a = f.readlines()
    hind = [float(x.split(",")[1]) for x in a]
df = {"tegelik hind": hind,"silutud hind":silu_andmed(hind,50),"X":range(1,len(hind)+1)}
fig = plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot("tegelik hind",data=df, color="blue")
ax.plot("silutud hind",data=df, color="orange")
#sns.lineplot(data=pd.melt(pd.DataFrame(),id_vars="X",value_vars=["tegelik hind","silutud hind"]), x="X", y="value",hue="variable")
plt.show()