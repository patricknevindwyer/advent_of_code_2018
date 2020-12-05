import sys


def read_barcodes(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().split("\n")
    

def contains_doubles(box_id):
    chars = list(set(box_id))
    
    for char_n in chars:
        if box_id.count(char_n) == 2:
            return True
    return False
    

def contains_triples(box_id):
    chars = list(set(box_id))
    
    for char_n in chars:
        if box_id.count(char_n) == 3:
            return True
    return False


def checksum(barcodes):
    twos = 0
    threes = 0
    
    for barcode in barcodes:
        if contains_doubles(barcode):
            twos += 1
        if contains_triples(barcode):
            threes += 1
    
    return twos * threes


if __name__ == "__main__":
    barcodes = read_barcodes(sys.argv[-1])
    csum = checksum(barcodes)
    print("checksum: %d" % (csum,))