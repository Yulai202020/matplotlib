from matplotlib import pyplot as plt
from data import *

# plt.xkcd() # как бутдо паписал человек
plt.style.use("fivethirtyeight")

plt.scatter(x,x_multby2) # пирог
plt.scatter(4,3,s=100,c="green",marker="X",alpha=0.5) # пирог

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("mygraph.png")