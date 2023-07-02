from matplotlib import pyplot as plt
from data import *

# plt.xkcd() # как бутдо паписал человек
plt.style.use("fivethirtyeight")

labels = ["1","2","3","4","5","6","7","8","9","10"]
explode = [0,0.5,0,0,0,0,0,0,0,0]
plt.pie(x, labels=labels, explode=explode, colors=colors, shadow=True) # пирог

plt.grid(True)
plt.tight_layout()

plt.savefig("mygraph.png")