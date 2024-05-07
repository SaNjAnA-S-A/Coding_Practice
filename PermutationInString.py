# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len or s2_len == 0:
            return False
        s1_dict = [0] * 26
        s2_dict = [0] * 26
        for i in range(s1_len):
            s1_dict[ord(s1[i])-ord('a')] += 1
            s2_dict[ord(s2[i])-ord('a')] += 1
        for i in range(s1_len,s2_len):
            if s1_dict == s2_dict:
                return True
            else:
                s2_dict[ord(s2[i-s1_len])-ord('a')] -= 1
                s2_dict[ord(s2[i])-ord('a')] += 1
        if s1_dict == s2_dict:
            return True
        else:
            False




        
