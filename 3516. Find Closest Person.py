class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        c1, c2 = abs(x-z), abs(y-z)

        if c1 == c2:
            return 0
        elif c1 < c2:
            return 1
        else:
            return 2
          
