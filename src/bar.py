from matplotlib import pyplot as plt
from data import *

# plt.xkcd() # как бутдо паписал человек
plt.style.use("fivethirtyeight")

plt.bar(x, x_multby2, color = "k", label="2x") # столбцы с низу
# plt.barh(x, x_multby2, color = "k", label="2x") # столбцы с бока

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("mygraph.png")