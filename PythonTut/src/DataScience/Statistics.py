__author__ = 'v11424'
import random
from matplotlib import pyplot as plt
from collections import Counter

def mean(x):
    return sum(x)/len(x)
#middle-most value of v
def median(v):
    n=len(v)
    sorted_v= sorted(v)
    midpoint=n//2
    if n%2==1:
        return sorted_v[midpoint]
    else:
        lo=midpoint-1
        hi=midpoint+1
        return (sorted_v[lo]+sorted_v[hi])/2
#pth-percentile value in x
def quantile(x, p):
    p_index=int(p*len(x))
    return sorted(x)[p_index]
#most-commom value(s)
def mode(x):
    count=Counter(x)
    max_count=max(count.values())
    return [x_i for x_i, count in count.iteritems()
            if count==max_count]
num_friends=[random.choice(range(100)) for _ in range(50)]
print(num_friends)
friend_counts=Counter(num_friends)
print(friend_counts)
xs=range(101)
ys=[friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0,101,0,25])
plt.title("Histogram of friend counts")
plt.xlabel("# of friend")
plt.ylabel("# of people")
plt.show()
