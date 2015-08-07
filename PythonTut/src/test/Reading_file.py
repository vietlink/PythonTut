'''
Created on 7 Aug 2015

@author: v11424
'''
from sys import argv


if __name__ == '__main__':
    argv=input("imput argument: ").split()
    script, filename= argv
    txt= open(filename)
    print("Here is your file %r: " %filename)
    print(txt.read())
    print("Type the filename again:")
    file_again=input(">")
    txt_again= open(file_again)
    print(txt_again.read())