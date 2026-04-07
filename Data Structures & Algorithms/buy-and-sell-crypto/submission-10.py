class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i,j = 0,1
        mx = 0
        n = len(prices)
        while j<n:
            if prices[i] < prices[j]:
                temp = prices[j] - prices[i]
                mx = max(temp,mx)
            elif prices[i]>prices[j]:
                i = j
            j+=1
            
        return mx
                
        