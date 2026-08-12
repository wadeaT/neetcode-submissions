class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        
        temp = []
        i = 0
        for num in freq:
            temp.append((freq[num],num))
        temp.sort()
        res = []
        for i in range(k):
            res.append(temp[len(temp)-i-1][1])
        return res
