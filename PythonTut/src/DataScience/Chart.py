__author__ = 'v11424'
from matplotlib import pyplot as plt
#line chart
years=[1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp=[300.2, 432.4, 533.5, 673.4, 634, 564, 500]
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("Nominal GDP")
plt.ylabel("Bilions of $")
plt.show()
#bar chart
movies=["Anna Hall", "Ben-Hur","Casanblanca", "Gandhi"]
num_oscars=[5, 11, 3, 5]
xs= [i+0.1 for i, _ in enumerate(movies)]
plt.bar(xs, num_oscars)
plt.ylabel("# of Academic Award")
plt.title("My fav film")
plt.xticks([i+0.5 for i, _ in enumerate(movies)], movies)
plt.show()
#line charts
variance=[1,2,4,8,16,32,64,128,256]
bias_squared=[256,128,64,32,16,8,4,2,1]
total_err=[x+y for x, y in zip(variance, bias_squared)]
xs=[i for i, _ in enumerate(variance)]
plt.plot(xs, variance, 'g-', label='variance')
plt.plot(xs, bias_squared, 'r-', label='bias^2')
plt.plot(xs, total_err, 'b:', label='total error')
plt.legend(loc=9)
plt.xlabel("model complexity")
plt.title("The Bias-Variance Tradeoff")
plt.show()
#scsatterplot
friends=[70,65,72,63,71,64,60,64,67]
minutes=[175,170,205,120,220,130,105,145,190]
labels=['a','b','c','d','e','f','g','h','i']
plt.scatter(friends,minutes)
for label, friend_count, minute_count in zip(labels, friends,minutes):
    plt.annotate(label, xy=(friend_count,minute_count),
                 xytext=(5,-5),
                 textcoords='offset points')
plt.title("Daily minutes vs No of friends")
plt.xlabel("# of friend")
plt.ylabel("Daily minutes spent on site")
plt.show()
