class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst = []
        for i in nums:
            i = i**2
            lst.append(i)
        lst.sort()
        return lst
    