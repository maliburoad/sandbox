# -*- coding: utf-8 -*-

#==============#
#= Easy Rider =#
#==============#

import re
import logging
import sys

inputText = "Hello 09-12-1979 World 15-12-1979 test 22-12-1979"
regex = "[0-9]{2}-[0-9][1-2]-1979"

#a, b, c = sys.argv
#print b, c

def write(input):
    logging.debug('writing to file')
    #print "def write"
    file = open('tekst.txt','w')
    file.write(input)
    file.close()

def read():
    logging.debug('reading the file')
    #print "def read"
    file = open('tekst.txt', 'r')
    output = file.read()
    file.close()
    return output
    
def checkTheFile(input, regex):
    logging.debug('searching the occurences od RE')
    output = re.findall( r'%s' % regex, input) 
    items = len(output)
    if output:
       print 'Found %s items: %s' % (items, output)
       logging.info('Found %s items: %s' % (items, output))     
    else:
       print "No match"         
    return output

def replace(input, regex):
    logging.debug('replace the occurences of RE')
    #print "def replace"
    output = re.sub( r'%s' % regex, 'dupa', input)       
    return output   

def main():
    logging.basicConfig(filename='rider.log', format='%(levelname)s %(asctime)s %(message)s', filemode = 'w', level=logging.DEBUG)
    write(inputText)
    a = read() 
    checkTheFile(a, regex)
    b = replace(a, regex)
    write(b)
    print 'Modified: ',read()
    
if __name__ == "__main__": main()
