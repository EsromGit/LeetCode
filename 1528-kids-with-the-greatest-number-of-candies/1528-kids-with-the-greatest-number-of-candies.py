class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1 = max(candies)
        return [(candy + extraCandies)>= max1 for candy in candies]                    