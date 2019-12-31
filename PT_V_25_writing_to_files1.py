#writing to files

#with open('penguins.jpg', 'rb') as rf:
#    with open('penguins_copy.jpg', 'wb') as wf:
#        for line in rf:
#            wf.write(line)

#In order to do this in chunks
with open('penguins.jpg', 'rb') as rf:
    with open('penguins_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
            

