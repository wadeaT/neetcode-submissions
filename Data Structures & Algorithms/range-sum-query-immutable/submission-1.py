class NumArray:
    #prefix sum solution - O(n) 
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        temp = 0
        for i in range(len(self.nums)):
            temp += self.nums[i]
            self.prefix.append(temp)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)