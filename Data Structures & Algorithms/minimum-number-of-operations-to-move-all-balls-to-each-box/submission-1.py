class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        dic = {1:[]}

        n = len(boxes)
        for i in range(n):
            if int(boxes[i]) == 1:
                dic[1].append(i)
        
        answer = [0] * n

        for i in range(n):
            for num in dic[1]:
                answer[i] += abs(i-num)
        return answer