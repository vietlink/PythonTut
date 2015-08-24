__author__ = 'v11424'
import random
from matplotlib import pyplot as plt
from collections import Counter
num_friends=[random.choice(range(100)) for _ in range(50)]
print(num_friends)
friend_counts=Counter(num_friends)
print(friend_counts)
xs=range(101)
ys=[friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0,101,0,25])
plt.title("Histogram of friend counts")
plt.xlabel("# of friengd")
plt.ylabel("# of people")
plt.show()
