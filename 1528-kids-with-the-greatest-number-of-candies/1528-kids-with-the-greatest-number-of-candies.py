class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        max1 = 0
        for i in candies:
            if max1 < i:
                max1 = i
                
        for i in candies:
            i += extraCandies
            if i < max1:
                lst.append(False)
            else:
                lst.append(True)
        return lst                    