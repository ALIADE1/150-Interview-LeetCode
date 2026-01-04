class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def fun(arr):
            bin_cou = bin(arr).count('1')
            return (bin_cou,arr)
        
        arr.sort(key = fun)
        return arr
