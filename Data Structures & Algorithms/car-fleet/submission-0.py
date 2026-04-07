class Solution:
    def carFleet(self, target: int, arr: List[int], speed: List[int]) -> int:
        pairArr = [0] * len(arr)
        for i in range(len(arr)):
            pairArr[i] = [arr[i],speed[i]]
        
        pairArr.sort(reverse=True)

        

        stack = []
        for i in range(len(pairArr)):
            p,s  = pairArr[i]
            t = (target - p)/s

            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            



            
            


        