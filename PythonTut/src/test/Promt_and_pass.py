'''
Created on 7 Aug 2015

@author: v11424
'''
from sys import argv

prompt= '>'
if __name__ == '__main__':
    #get input from command line
    argv= input("enter input argument").split()
    script, username= argv
    #
    print("Hi %s, I'm the %s script" %(username, script))
    print("I'd like to ask you a few question")
    print("Do you like me, %s" %username)
    likes= input(prompt)
    print("Where do you live, %s" %username)
    lives= input(prompt)
    print("What kind of computer you have %s" %username)
    computer= input(prompt)
    print("Alright, you said %r about liking me. You live in %s and you have a %s computer" %(likes, lives, computer))
    