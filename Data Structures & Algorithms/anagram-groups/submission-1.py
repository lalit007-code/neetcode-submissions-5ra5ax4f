from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n == 0 or n == 1:
            return [strs]
        hash_ans = defaultdict(list)
        for i in strs:
            count = [0]*26
            for char in i:
                count[ord(char)-ord('a')]+=1
            hash_ans[tuple(count)].append(i)
        # print(hash_ans)
        # return [hash_ans]
        return list(hash_ans.values())


        