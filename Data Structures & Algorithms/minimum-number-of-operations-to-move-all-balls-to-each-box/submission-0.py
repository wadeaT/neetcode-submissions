class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        #prefix and suffix sum
        n = len(boxes)
        prefix = [0] * (n+1)
        suffix = [0] * (n+1)
        sumPrefix = 0
        sumSufix = 0
        for i in range(n):
            sumPrefix += int(boxes[i])
            prefix[i] = sumPrefix
            sumSufix += int(boxes[n-i-1])
            suffix[n-i-1] = sumSufix
        
        answer = [0] * n

        for i in range(n):
            for j in range(i+1,n):
                answer[i] += suffix[j]
            for j in range(i):
                answer[i] += prefix[j]
        return answer