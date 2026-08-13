class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        s = set()

        mul = 1
        n =len(nums)
        for i in range(n):
            if nums[i] != 0 :
                mul *= nums[i]
            else:
                s.add(i)
        output = [0] * n
        if len(s) == 0:
            for i in range(n):
                output[i] = mul // nums[i]
            
        elif len(s) == 1:
            output[list(s)[0]] = mul
        
        return output