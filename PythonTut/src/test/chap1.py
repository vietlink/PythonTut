'''
Created on 7 Jan 2015

@author: v11424
'''
from pip._vendor.distlib.compat import raw_input
def write_file(outfilename):
    outfile= open(outfilename, 'w')
    outfile.write('Line 1 \n')
    outfile.write('Line 2 \n')
    outfile.write('Line 3 \n')
    outfile.close()

def append_file(oufilename):
    outfile= open(oufilename, 'a')
    outfile.write('Line 4 \n')
    outfile.write('Line 5 \n')
    outfile.close()
    
def read_file(infilename):
    infile= open(infilename, 'r')
    for line in infile:
        print(line.rstrip())
    infile.close()
    
def testArgLists_1 (*arg, **kwargs):
    print('args: ', arg)
    print('kwarg:', kwargs)
testArgLists_1('aaa', 'bbb', arg1='ccc', arg2='ddd')
def testArgLists_2 (arg0, *arg, **kwargs):
    print('arg0: "%s"'%arg0)
    print('args: ', arg)
    print('kwarg:', kwargs)
def test():
    testArgLists_1('aaa', 'bbb', arg1='ccc', arg2='ddd')
    print('='*40)
    testArgLists_2('a first argument', 'aaa', 'bbb', arg1='ccc', arg2='ddd')
test()
    
    