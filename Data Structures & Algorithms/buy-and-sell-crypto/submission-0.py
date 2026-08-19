class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force 

        n = len(prices)
        maxPro = 0
        for i in range(n):
            for j in range(i+1,n):
                if (prices[j] - prices[i]) > maxPro:
                    maxPro = prices[j] - prices[i]
        
        return maxPro
