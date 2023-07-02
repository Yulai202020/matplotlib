from matplotlib import pyplot as plt
from collections import Counter
import csv

with open("data.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lauguege = Counter()
    for row in csv_reader:
        lauguege.update(row[""].split(";"))


laugueges = []
popularity = []

for item in lauguege.most_common(15):
    laugueges.append(item[0])
    popularity.append(item[0])

plt.grid(True)
plt.legend()

plt.savefig("mygraph.png")