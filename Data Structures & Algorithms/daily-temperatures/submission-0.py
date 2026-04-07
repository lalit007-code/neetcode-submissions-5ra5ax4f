class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack = []
        res  = [0] * len(arr)

        for i in range(len(arr)):
            while stack and stack[-1][1] < arr[i]:
                print("stack",stack[-1][1])
                print("arr",arr[i])
                print("while condition")
                temp = stack.pop() # [idx,val]
                print("temp",temp)
                res[temp[0]] = i - temp[0]
                temp.clear()
            stack.append([i,arr[i]])
            print("outisde whiule stack",stack)
        # print(stack)
        return res




