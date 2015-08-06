'''
Created on 6 Aug 2015

@author: v11424
'''
x= "There are %d types of people" %10
binary= "binary"
do_not= "don't"
y="Those who know %s and those who %s" %(binary, do_not)

if __name__ == '__main__':
    print (x)
    print(y)
    print("I said: %r " %x)
    print("I also said: '%s'" %y)
    
    hilarious=False
    joke_eval= "Isn't that joke so funny? %r"
    print(joke_eval %hilarious)
    w="This is the left side of ....."
    e= "a string with a right side"
    print (w+e)