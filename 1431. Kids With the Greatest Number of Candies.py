class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxx = max(candies)
        results = []

        for x in candies:
            if x + extraCandies >= maxx:
                results.append(True)
            else:
                results.append(False)

        return results
