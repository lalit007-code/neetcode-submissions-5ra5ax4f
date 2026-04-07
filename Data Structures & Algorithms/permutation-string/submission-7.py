
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == "":
            return True
        
        s1freq = {}
        for c in s1:
            s1freq[c] = s1freq.get(c,0)+1
        s1_len = len(s1)
        freq = {}
        i = 0

        for j in range(len(s2)):
            #always checking this 
            char_i = s2[i]
            char_j = s2[j]
            
            freq[char_j] = freq.get(char_j,0)+1

            # print("s1_freq",s1freq)
            # print("s2_freq",freq)
            if s1freq == freq:
                return True

            while s1_len == (j-i+1):
                # print(char_i)
                # print(freq)
                freq[char_i]-=1
                if freq[char_i] < 1:
                    del freq[char_i]
                i+=1            
        return False
            

            

        