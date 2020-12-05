#!/usr/bin/python
import sys

def read_numbers(filepath):
    nums = []
    
    for line in open(filepath, "r").read().split("\n"):
        if line.startswith("+"):
            nums.append(int(line[1:]))
        elif line.startswith("-"):
            nums.append(-1 * int(line[1:]))
    print "Read %d numbers" % (len(nums))
    return nums
    
if __name__ == "__main__":

    f = sys.argv[-1]
    
    b = 0
    for n in read_numbers(f):
        b += n
    print b
    