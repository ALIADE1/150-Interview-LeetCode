class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        trip_list = [0] * (n+1)
        trip_list[0] = 0

        for x in range(1, n+1):
            trip_list[x] = trip_list[x-1] + gain[x-1]

        return max(trip_list)
