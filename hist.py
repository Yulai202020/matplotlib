from matplotlib import pyplot as plt
from data import *

# plt.xkcd() # как бутдо паписал человек
plt.style.use("fivethirtyeight")

labels = ["1","2","3","4","5","6","7","8","9","10"]
explode = [0,0.5,0,0,0,0,0,0,0,0]
plt.hist(x, bins=[0,1,2,4,5,6] ) # пирог

plt.grid(True)
plt.tight_layout()

plt.savefig("mygraph.png")