import sys


def read_barcodes(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read().split("\n")
    

def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]


def find_barcode_matches(barcodes):
    
    for idx_a in range(len(barcodes)):
        for idx_b in range(idx_a + 1, len(barcodes)):
            barcode_a = barcodes[idx_a]
            barcode_b = barcodes[idx_b]
            
            if levenshteinDistance(barcode_a, barcode_b) == 1:
                yield barcode_a, barcode_b

def intersect_barcodes(barcode_a, barcode_b):
    
    rebuilt = []
    
    for idx in range(len(barcode_a)):
        if barcode_a[idx] == barcode_b[idx]:
            rebuilt.append(barcode_a[idx])
    return "".join(rebuilt)
    

if __name__ == "__main__":
    
    barcodes = read_barcodes(sys.argv[-1])
    
    for (ba, bb) in find_barcode_matches(barcodes):
        print("%s\n%s\n%s\n---" % (ba, bb, intersect_barcodes(ba, bb)))
    
    