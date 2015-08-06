'''
Created on 6 Aug 2015

@author: v11424
'''
from sys import argv

if __name__ == '__main__':
    argv= input("enter input argument").split()
    script, first, second, third= argv
    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)
    print("Your third variable is:", third)