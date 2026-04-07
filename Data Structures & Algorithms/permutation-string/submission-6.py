from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)< len(s1):
            return False
        f1 = Counter(s1)
        f2 = {}
        l = 0
        
        r = 0
        print("f11",f1)
        while r<len(s2):
            f2[s2[r]] = 1 + f2.get(s2[r],0)

            while r-l+1 > len(s1):
                f2[s2[l]] -=1
                if f2[s2[l]] == 0:
                    del f2[s2[l]]
                l+=1
            print("f2",f2)

            if r-l+1 == len(s1) and f2 == f1:
                return True
            r+=1
        return False
