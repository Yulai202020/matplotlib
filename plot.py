from matplotlib import pyplot as plt
from data import *

# plt.xkcd() # как бутдо паписал человек
plt.style.use("fivethirtyeight")

plt.plot(x, square, color = "b", linestyle="--", linewidth=2, label="x") # график линеями; деление от x и x^2 на графике
plt.plot(x, x_multby2, color = "k", linestyle="--", linewidth=2, label="x") # график 2x
plt.plot(x, x, color = "k", linestyle="--", linewidth=2, label="x") # график x

plt.fill_between(x,x_multby2,square)

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("mygraph.png")