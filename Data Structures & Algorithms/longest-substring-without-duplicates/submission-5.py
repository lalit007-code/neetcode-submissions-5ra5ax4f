class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i,j = 0,0
        n = len(s)
        h = set()
        res = float('-inf')
        count = 0

        while j<n:
            if s[j] in h:
                h.remove(s[i])
                i+=1
                continue
            else:
                h.add(s[j])
            print("i--",i)
            print("j--",j)
            res = max(res,j-i+1)
            j+=1
            print("set",h)
            print("res",res)

            
        return res

        