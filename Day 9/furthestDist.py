class Solution:
    def furthestDistanceFromOrigin(self, m: str) -> int:
        l,r=m.count('L'),m.count('R')
        if l>r:
            return len(m)-2*r
        elif r>l:
            return len(m)-2*l
        else:
            return len(m)-2*r
        