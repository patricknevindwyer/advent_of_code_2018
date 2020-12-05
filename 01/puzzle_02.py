#!/usr/bin/python
import sys

def read_numbers(filepath):
    nums = []
    
    for line in open(filepath, "r").read().split("\n"):
        if line.startswith("+"):
            nums.append(int(line[1:]))
        elif line.startswith("-"):
            nums.append(-1 * int(line[1:]))
    print("Read %d numbers" % (len(nums)))
    return nums

def cycle_until_repeated(numbers):
    
    seen = set()
    running = True
    repeated = None
    current = 0
    seen.add(current)
    
    while running:
        for number in numbers:
            current = current + number
            
            # do we have our duplicate?
            if current in seen:
                repeated = current
                running = False
                break
            seen.add(current)
    
    return repeated
    
    
if __name__ == "__main__":

    f = sys.argv[-1]
    
    repeated = cycle_until_repeated(read_numbers(f))
    print(repeated)
    