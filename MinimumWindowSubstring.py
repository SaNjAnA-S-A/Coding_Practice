# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #t_count, s_count = {}, {}
        s_count = {}
        char_count, min_count = 0, float('inf')
        output_ind = [-1,-1] # left and right index of the output string window
        left = 0
        # store the char frequency of t
        #for i in t:
        #    t_count[i] = 1 + t_count.get(i,0)
        t_count = Counter(t)
        for j in range(len(s)):
            k = s[j]
            # store the char frequency of s
            s_count[k] = 1 + s_count.get(k,0)
            if k in t and s_count[k] == t_count[k]:
                # if the char is present in t with same frequency then increment the counter
                char_count += 1
        
            while char_count == len(t_count):
                # When all the frequencies of s match with t then update minimum window
                if min_count > (j - left + 1):
                    min_count = j - left + 1
                    output_ind = [left, j]
                
                # Remove the left most character from window
                s_count[s[left]] -= 1
                # if the removed char is present in t and the frequency is reduced then decrement the counter
                if s[left] in t and s_count[s[left]] < t_count[s[left]]:
                    char_count -= 1
                left += 1
        return s[output_ind[0]:output_ind[1]+1] if min_count != float('inf') else ""
