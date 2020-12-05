import sys


def parse_claims(filename):
    
    with open(filename, "r", encoding="utf-8") as f:
        raw = f.read()
    
    claims = []
    for line in raw.split("\n"):
        c_num, rest = line.split("@")
        offset, area = rest.split(":")
        
        off_left, off_top = offset.split(",")
        area_width, area_height = area.split("x")
        
        claims.append(
            {
                "claim": c_num.strip(),
                "left": int(off_left.strip()),
                "top": int(off_top.strip()),
                "width": int(area_width.strip()),
                "height": int(area_height.strip())
            }
        )
    return claims
    

class Fabric:
    
    def __init__(self, width=1000, height=1000):
        self._fabric = []
        
        for idx in range(height):
            row = []
            for idx_b in range(width):
                row.append(0)
            self._fabric.append(row)
    
    def get_claim_count_at(self, x, y):
        return self._fabric[y][x]
    
    def add_claim_at(self, x, y):
        self._fabric[y][x] += 1
    
    def add_claim(self, left, top, width, height):
        
        for w in range(width):
            for h in range(height):
                self.add_claim_at(left + w, top + h)
    
    def count_multi_claims(self):
        count = 0
        for h in range(len(self._fabric)):
            for w in range(len(self._fabric[0])):
                if self._fabric[h][w] > 1:
                    count += 1
        return count
    
    def display(self):
        for row in self._fabric:
            print("".join(["%d"% (c,) for c in row]))
            
    def has_overlap(self, left, top, width, height):
        laps = []
        for w in range(width):
            for h in range(height):
                laps.append(self.get_claim_count_at(left + w, top + h))
        
        lapped = set(laps)
        return lapped != set([1])
        
        
if __name__ == "__main__":
    claims = parse_claims(sys.argv[-1])
    
    # create the fabric
    fabric = Fabric()
    for claim in claims:
        fabric.add_claim(claim["left"], claim["top"], claim["width"], claim["height"])
    
    # check for anything with no overlaps
    for claim in claims:
        if not fabric.has_overlap(claim["left"], claim["top"], claim["width"], claim["height"]):
            print("claim %s has no overlap" % (claim["claim"],))
                
