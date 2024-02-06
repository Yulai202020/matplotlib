from data import *
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")

plt.plot(x,x)

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("mygraph.png")