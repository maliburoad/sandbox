File operation

f = open('workfile', 'r') #the file will only be read
f = open('workfile', 'w') #only writing (an existing file with the same name will be erased)
f = open('workfile', 'a') #opens the file for appending
f = open('workfile', 'r+') #opens the file for both reading and writing.

#The mode argument is optional; 'r' will be assumed if it’s omitted.
#To create file use 'w' mode

Reading file (file object f)
f.read () #
f.readline () #reads a single line from the file; a newline character (\n) is left at the end of the string
f.readlines () #


#For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:
for line in f:
        print line,