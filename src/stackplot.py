from matplotlib import pyplot as plt
from data import *

# plt.xkcd() # как бутдо паписал человек
plt.style.use("fivethirtyeight")

plt.stackplot(x,x_multby2,square, colors=colors) # деление от x; x_multby и square на графике

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Test title") 

plt.grid(True)
plt.tight_layout()

plt.savefig("mygraph.png")