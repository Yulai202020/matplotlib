from matplotlib import pyplot as plt
from data import *

# plt.xkcd() # как бутдо паписал человек
plt.style.use("fivethirtyeight")

fig, (sub1, sub) = plt.subplots(nrows=2, ncols=1)

sub.scatter(x,x_multby2) # пирог
sub1.scatter(4,3,s=100,c="green",marker="X",alpha=0.5) # пирог

sub.grid(True)
sub1.grid(True)

plt.savefig("mygraph.png")