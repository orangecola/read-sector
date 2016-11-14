#!/usr/bin/python

import sys

def usage():
    print 'Usage: read-sector.py file'
    exit()
    
def main():
    if (len(sys.argv) != 2):
        usage()
    else:
        try:
            f = open(sys.argv[1])
        
        except:
            usage()
        
        else:
            print (sys.argv[1])
            
if __name__ == "__main__":
    main()