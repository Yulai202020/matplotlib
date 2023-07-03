from matplotlib import pyplot as plt
from data import *

# plt.xkcd() # как бутдо паписал человек
plt.style.use("fivethirtyeight")
a = [2,5,7,8,10,11,10,5]
plt.hist(a, edgecolor='black') # пирог

plt.grid(True)
plt.tight_layout()

plt.savefig("mygraph.png")