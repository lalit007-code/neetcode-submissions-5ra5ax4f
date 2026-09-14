class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] 

        for i in range(len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][1] < t :
                idx,val = stack.pop()
                ans[idx] = i-idx
            stack.append([i,temperatures[i]])
        
        return ans

                
