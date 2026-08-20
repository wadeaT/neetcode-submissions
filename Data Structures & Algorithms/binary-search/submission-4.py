class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        left = 0
        right = len(nums) -1 

        while left<=right:
            mid = left + (right - left) // 2
            temp = nums[mid]
            if temp == target:
                return mid
            elif temp > target : 
                right = mid - 1 
            elif temp < target: 
                left = mid + 1 
            
        return -1