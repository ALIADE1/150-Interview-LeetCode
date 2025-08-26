class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        dig_, area_ = 0, 0

        for i, j in dimensions:
            dig = sqrt(i*i + j*j)
            area = i * j

            if dig > dig_ or (dig == dig_ and area > area_):
                dig_ = dig
                area_ = area

        return area_
      
