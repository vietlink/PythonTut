'''
Created on 9 Jan 2015

@author: v11424
'''
import sys, re
from pip._vendor.distlib.compat import raw_input
import linecache
# nhap vao mot chuoi va so sanh voi aa[bc]*dd
def compileRegularExp():
    pat= re.compile('aa[bc]*dd')
    while 1:
        line= raw_input('Enter a line ("q" to quit)')
        if (line=='q'):
            break
        if pat.search(line):
            print('matched:', line)
        else:
            print('no match: ', line)
#trich rut gia tri so trong cau
def extractValue():
    targets= ['There are <<25>> sparrows',
              'I see <<15>> finches',
              ' There is nothing here']
    pat= re.compile('<<([0-9]*)>>')
    for line in targets:
        mo= pat.search (line)
        if mo:
            value= mo.group (1)
            print('Value: %s' % value )
        else:
            print('no match')     
# trich rut nhieu gia tri
def extractMultiItems():
    pat= re.compile('aa([0-9]*)bb([0-9]*)cc')
    while 1:
        line= raw_input('Enter a line ("q" to quit)')
        if line=='q':
            break
        mo=pat.search(line)
        if mo:
            value1, value2= mo.group(1, 2)
            print('value1: %s value2: %s' %(value1, value2))
        else:
            print('no matched')
#thay the ki tu
def replc_func(mo):
    s1=mo.group(1)
    s2='*'*len(s1)
    return s2
def replaceItems():
    pat= r'(\d+)'
    in_str= 'there are 1024 birds in 1000 trees'
    out_str, count=re.subn(pat, replc_func, in_str)
    print ('in: %s' %in_str)
    print('out: %s'%out_str)
    print('count: %d' %count)
    
def replacesItems1():
    pat= re.compile('aa([0-9]*)bb([0-9]*)cc')
    while 1:
        line= raw_input('Enter a line ("q" to quit): ')
        if line=='q':
            break
        mo= pat.search(line)
        if mo:
            value1, value2= mo.group(1,2)
            start1= mo.start(1)
            end1= mo.end(1)
            start2= mo.start(2)
            end2= mo.end(2)
            print('value1: %s start1: %s end1: %s' %(value1, start1, end1))
            print('value2: %s start2: %s end2: %s' %(value2, start2, end2))
            repl1= raw_input('enter replacement #1: ')
            repl2= raw_input('enter replacement #2: ')
            newline= (line[:start1]+repl1+line[end1:start2]+repl2+line[end2:])
            print('new line: %s' %newline)
        else:
            print('no match')
def subtituteItems():
    pat=re.compile('([0-9])+')
    print('Replace decimal digits')
    while 1:
        target= raw_input('Enter a String ("q" to quit): ')
        if target=='q':
            break
        repl= raw_input('Enter a replacement: ')
        result= pat.sub(repl, target)
        print('Result: %s' % result)
            
#2.3 iteration
#1 generator function
def generateItems(seq):
    for item in seq:
        yield 'item: %s' %item
def generatorFunc():
    anIter= generateItems([])
    print('dir(anIter): ', dir(anIter))
    anIter= generateItems([222, 333, 444])
    for x in anIter:
        print(x)
    anIter= generateItems(['aaa', 'bbb', 'ccc'])
    print(anIter.__next__())
    print(anIter.__next__())
    print(anIter.__next__())
    print(anIter.__next__())
DATA=['lemon','lime','grape','apple','pear','watermelon','canteloupe','honeydew','orange','grapefruit']
def make_producer(collection, excludes):
    gen=(item for item in collection if item not in excludes)
    return gen 
def test():
    iter1= make_producer(DATA, ('apple', 'orange', 'honeydew'))
    print('%s' %iter1)
    for fruit in iter1:
        print(fruit)
#2. class with generator method  
class Node:
    def __init__(self, name='<noname>', value='<novalue>', children=None):
        self.name=name
        self.value=value
        self.children= children
        if (children is None):
            self.children=[]
        else:
            self.children=children   
    def set_name(self,name):self.name=name
    def get_name(self):return self.name     
    def set_value (self, value):self.value= value
    def get_value(self):return self.value
    def iterchildren(self):
        for child in self.children:
            yield child
    
    def walk(self, level=0):
        print('%sname: %s value: %s' %(get_filler(level), self.get_name(), self.get_value()))
        for child in self.iterchildren():
            child.walk(level+1)

def walk(node, level=0):
    print('%sname: %s value: %s' %(get_filler(level), node.get_name(), node.get_value()))
    for child in node.iterchildren():
        walk(child, level+1)
def get_filler(level):
    return ' '* level
def test1():
    a7= Node('gilbert', '777')
    a6=Node('fred', '666')
    a5=Node('ellie','555')
    a4=Node('daniel', '444')
    a3=Node('carl','333',[a4, a5])
    a2=Node('bill', '2222', [a6, a7])
    a1=Node('alice','111', [a2,a3])
    print('Using the method')
    a1.walk()
    print('='*30)
    print('Using the function')
    walk(a1)
if __name__=="__main__":
    test1()