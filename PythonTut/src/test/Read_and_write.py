'''
Created on 7 Aug 2015

@author: v11424
'''
from sys import argv

if __name__ == '__main__':
    argv= input("Enter argument").split()
    script, filename=argv
    print("we are going to erase %r" %filename)
    print("If you don't want that, hit ctrl-C")
    print("If you want that, hit RETURN")
    input("?")
    print("Opening the file.....")
    target= open(filename, 'w')
    print("Truncating the file.Goodbye!")
    target.truncate()
    print("Now T'm going to ask you for three lines")
    line1= input("line 1: ")
    line2= input("line 2: ")
    line3= input("line 3: ")
    print("I'm going to write these lines")
    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")
    print("And finally, we close it")
    target.close()