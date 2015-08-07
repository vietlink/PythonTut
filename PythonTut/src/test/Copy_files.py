'''
Created on 7 Aug 2015

@author: v11424
'''
from sys import argv
from os.path import exists #check if file exists

if __name__ == '__main__':
    argv= input("Enter argument: ").split()
    script, from_file, to_file= argv
    print("Copying from %s to %s" %(from_file, to_file))
    in_file= open(from_file)
    indata= in_file.read()
    print("The input file is %d bytes long" %len(indata))
    print("Does the output file exist? %r" %exists(to_file))
    print("Ready, hit RETURN  to continue, Ctrl-C to abort")
    input(">")
    out_file= open(to_file, 'w')
    out_file.write(indata)
    print("Alright, all done")
    out_file.close()
    in_file.close()
    