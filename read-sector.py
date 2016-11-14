#!/usr/bin/python

import time, os,sys

def split_list(n):
    """will return the list index"""
    return [(x+1) for x,y in zip(n, n[1:]) if y-x != 1]

def get_sub_list(my_list):
    """will split the list base on the index"""
    my_index = split_list(my_list)
    output = list()
    prev = 0
    for index in my_index:
        new_list = [ x for x in my_list[prev:] if x < index]
        output.append(new_list)
        prev += len(new_list)
    output.append([ x for x in my_list[prev:]])
    return output

def usage():
    print 'Usage: read-sector.py file'
    exit()
    
def main():
    if (len(sys.argv) != 2):
        usage()
    else:
        try:
            f = open(sys.argv[1], 'r')
        
        except:
            usage()
        
        #Initialize list of non-empty sectors
        nums = []
        
        #Find number of sectors in the file
        sectors = (os.path.getsize(sys.argv[1]) / 512)
        
        for i in range(sectors):
            result = False
            #for j in range(511):
            f.seek(i * 512,0)
            line = f.read(1).encode('hex')
            #Scan first value
            if (line != '00'):
                result = True
                
            
            if (result):
                print i
                nums.append(i)
            
        #Print the list of non-empty sectors
        nums = get_sub_list(nums)

            
if __name__ == "__main__":
    main()