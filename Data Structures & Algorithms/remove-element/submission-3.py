class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        j = len(nums)-1


        while(i<=j):
            if(nums[i] == val):
                while(nums[j] == val):
                    j-=1
                    if (j<i):
                        return i
                nums[i] = nums[j]
                j-= 1
                
            i += 1
        return j + 1