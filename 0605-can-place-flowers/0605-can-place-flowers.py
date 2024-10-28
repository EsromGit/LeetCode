class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        counter = 0
        pointer = 0
        while pointer < len(flowerbed):
            if (flowerbed[pointer] == 0 and 
            (pointer == 0 or flowerbed[pointer - 1] == 0) and 
            (pointer == len(flowerbed)-1 or flowerbed[pointer + 1] == 0)):
                counter += 1
                pointer += 2
            else:
                pointer += 1
        return counter >= n      