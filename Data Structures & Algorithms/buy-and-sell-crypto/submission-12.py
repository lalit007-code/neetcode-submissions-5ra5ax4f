class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        ans = 0
        while j < len(prices):
            # print(ans)
            # print("i",i,prices[i])
            # print(j,prices[j])
            if prices[i] > prices[j]:
                i = j
                j +=1
            else:
                ans = max(ans,prices[j]-prices[i]) 
                j+=1
        
        return ans