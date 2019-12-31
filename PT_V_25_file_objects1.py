# File Objects

##not the best option to open a file. Will need to be closed at the end!
#f = open('test.txt', 'r')
#
##print out file name
#print(f.name)
#
##print out the mode that the file was opened in
#print(f.mode)
#
#f.close()


#better to work with a context manager
with open('test.txt', 'r') as f:
    pass

print(f.name)
print(f.mode)