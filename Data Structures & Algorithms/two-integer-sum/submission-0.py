class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        appears = {}
        n = len(nums)
        for i in range(0,n):
            if (target-nums[i]) in appears:
                return [appears[target-nums[i]],i]
            appears[nums[i]] = i
            