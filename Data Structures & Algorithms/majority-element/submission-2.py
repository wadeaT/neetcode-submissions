class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pool = {}

        for num in nums: 
            if num in pool:
                pool[num] +=1 
            else:
                pool[num] = 1
        
        max = -1
        val = -1 
        for num1 in pool:
            if pool[num1] > max: 
                max = pool[num1]
                val = num1 
        return val