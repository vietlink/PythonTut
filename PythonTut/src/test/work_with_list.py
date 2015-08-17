__author__ = 'v11424'
ten_things="Apples Orange Crow telephone Light Sugar"
print("Wait, there's not 10 things in that list, let's fix that")
stuff= ten_things.split(" ")
more_stuff=["Day", "Night","song", "Frisbee", "Corn"]
while len(stuff)!=10:
    next_one=more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("There's %d items now" %len(stuff))
print("There we go: ", stuff)
print("let's do someting with stuffs")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))