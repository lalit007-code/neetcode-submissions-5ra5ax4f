class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        for c in range(len(s1)):
            count1[s1[c]] = 1 + count1.get(s1[c],0)
        need  = len(count1)
        for i in range(len(s2)):
            count2,c = {},0
            for j in range(i,len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j],0)
                if count1.get(s2[j],0) < count2[s2[j]]:
                    break
                print("count of s2[j]--",count1.get(s2[j]))
                # print(s1[j],s2[j])
                # print(j)
                
                if count1.get(s2[j],0) == count2[s2[j]]:
                    # print(s2[j])
                    # print(s2[j])
                    # print("count of s1[j]--",count1.get(s2[j]))
                    # print("count of s2[j]--",count2.get(s2[j]))
                    c+=1
                # print("count1--",count1)
                # print("count2--",count2)
                if c ==  need:
                    return True
        return False

                



        