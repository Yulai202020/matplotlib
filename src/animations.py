from random import randint
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("fivethirtyeight")

x = []
y = []
interval_ms = 1000
index = count()

def amination(i):
    x.append(next(index))
    x.append(randint(0, 5))

    plt.cla()
    plt.plot(x,y)

anim = FuncAnimation(plt.gcf(), amination, interval = interval_ms)


plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("mygraph.png")