class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        #brute force
        waitingTime = 0
        n = len(customers)
        if n<1:
            return 0
        temp = 0
        for customer in customers:
            temp = max(temp,customer[0])
            temp += customer[1]
            waitingTime += temp - customer[0]
        
        return waitingTime/n