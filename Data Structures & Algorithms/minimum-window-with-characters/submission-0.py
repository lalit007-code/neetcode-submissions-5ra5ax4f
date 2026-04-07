class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #handle edge where "t" is empty string
        # then decalring two hash variable , "countT" and another is to track our "window"
        # then we intitlaize 2 variable ,named as "need" and "value", where need equals to len(countT)
        #then we start traversing on "s", and maintaing "window" by pushing the element in our "window"
        #we increment the "have" value by comparing our "window" char value with countT value, if it equals then 
        #       we increment it by 1
        # while "have" == "need", then we update our value of "result" and "reslen" variable
        #we start incrementing our "l" pointer to right and in while condition
        #.      we will check if this char lie in "countT" then we dcrement it by 1 and then
        # we again check if it exist in out "countT" and if it is less then in countT then
        #.     we decrement our "have" 
        # increment out l 

        if t == "" or len(s) < len(t):
            return ""

        countT,window = {},{}

        for c in t:
            countT[c] = countT.get(c,0) + 1

        need,have = len(countT),0

        res,resLen  = [-1,-1],float('inf')
        l=0
        for r in range(len(s)):
            # add in window
            c = s[r]
            window[c] = window.get(c,0)+1
            
            if c in countT and window[c] == countT[c]:
                have+=1
            
            while have == need:
               

                #we have to check if our resLen is maximum by current len
                if resLen > (r-l+1):
                    res = [l,r]
                    resLen = (r-l+1)
                
                # wrong pop before
                window[s[l]] -=1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                
                l+=1

        l,r = res
        print(res)

        return s[l:r+1] if resLen != float('inf') else ""

                