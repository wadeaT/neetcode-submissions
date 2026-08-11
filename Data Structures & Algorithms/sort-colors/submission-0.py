class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # brute force

        appearance = {}

        for num in nums: 
            if num in appearance:
                appearance[num] +=1
            else:
                appearance[num] = 1
        
        index = 0
        for key in range(0,3):
            if key in appearance: 
                for i in range(appearance[key]):
                    nums[i+ index] = key
                index += appearance[key]
                    