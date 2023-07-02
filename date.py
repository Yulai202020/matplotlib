from matplotlib import pyplot as plt
from data import *
from datetime import datetime, timedelta
from matplotlib import dates as plt_dates
# plt.xkcd() # как бутдо паписал человек
plt.style.use("fivethirtyeight")

dates = [
    datetime(2020,4,6),
    datetime(2020,6,8),
    datetime(2020,8,10),
]

y = [4,3,5]

plt.plot_date(dates,y,linestyle="solid") # пирог
plt.gcf().autofmt_xdate()

date_format = plt_dates.DateFormatter("%b, %d %Y")
plt.gca().xaxis.set_major_formatter(date_format)

plt.grid(True)
plt.tight_layout()

plt.savefig("mygraph.png")