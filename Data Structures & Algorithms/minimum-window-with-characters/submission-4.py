class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s):
            return ""
        
        window = {}
        thash = {}

        for i in t:
            thash[i] = thash.get(i,0) + 1
        # print("thash",thash)
        have = 0
        need = len(thash)

        l = 0

        minL = float('inf')
        startingIndex = -1

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in thash and window[c] == thash[c]:
                have+=1
            
            while have == need:
                # print("l",l)
                if minL > r-l+1:
                    minL = r-l+1
                    startingIndex = l
                
                window[s[l]] = window.get(s[l],0)-1
                 
                # kya humne jo htya hai, uske wajah se kio effect padha hai ki ni
                if s[l] in thash and window[s[l]] < thash[s[l]]:
                    have-=1

                l+=1
        # print(startingIndex)
        
        # st = s[startingIndex:startingIndex+minL]
        # print(st)
        return "" if startingIndex == -1 else s[startingIndex:startingIndex+minL]





