class Solution:
    def isValid(self, s: str) -> bool:
        mpp = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        arr = []
        r = 0
        while r < len(s):
            if s[r] in mpp and arr:
                if arr[-1] != mpp[s[r]]:
                    return False
                else:
                    arr.pop()
                    r+=1
                    continue
            arr.append(s[r])
            r+=1
        return True if len(arr) == 0 else False