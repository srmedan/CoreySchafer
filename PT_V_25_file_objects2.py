#with open('test.txt', 'r') as f:
#    f_contents = f.read()
#    print(f_contents)

#print every line of the file
#with open('test.txt', 'r') as f:
#    f_contents = f.readlines()
#    print(f_contents)
    
#print the lines in the file one by one
#with open('test.txt', 'r') as f:
#    f_contents = f.readline()
#    print(f_contents, end='')
#    
#    f_contents = f.readline()
#    print(f_contents, end='')


#with open('test.txt', 'r') as f:
#    for line in f:
#        print(line, end='')


with open('test.txt', 'r') as f:
    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    print(f_contents, end='*')
    f.seek(0)
    f_contents = f.read(size_to_read)
    print(f_contents, end='*')
    
 
#    while len(f_contents) > 0:
#        print(f_contents, end='*')
#        f_contents = f.read(size_to_read)
        