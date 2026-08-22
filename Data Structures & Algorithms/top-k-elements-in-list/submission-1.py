class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        n = len(nums)
        arr = []
        for i in range(n):
            arr.append(set())
        
        for num in nums:
            if num in freq:
                arr[freq[num]-1].remove(num)
                freq[num] +=1
                arr[freq[num]-1].add(num)
            else:
                freq[num] = 1
                arr[0].add(num)
            
        number = 0
        result = []
        j = n-1
        while (number < k and j>=0):
            if arr[j] != []:
                number += len(arr[j])
                result += arr[j]
                if number == k:
                    return result
            j-=1
        return None
