class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Sorted Array
        #Find target in Array

        #Want to calulate the mid point, get the index if midpoint is equal to target

        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left+right) // 2
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m - 1
            else:
                return m 
        return -1
