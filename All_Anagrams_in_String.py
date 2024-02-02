""" https://leetcode.com/problems/find-all-anagrams-in-a-string/
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        s_len = len(s)
        p_len = len(p)
      
        # return [] if no anagrams found as s < p
        if s_len < p_len:
            return output
          
        # Count of characters in p
        p_cnt = Counter(p)
        # Count of characters in a part of s
        s_cnt = Counter(s[:p_len - 1])

        # Iterate over 's', starting from index where first full window can begin
        for i in range(p_len - 1, s_len):
            s_cnt[s[i]] += 1
            if p_cnt == s_cnt:
                # Anagram is found, record the index 
                output.append(i - p_len + 1)
            # Decrement the count of first character of window
            s_cnt[s[i - p_len + 1]] -= 1
            # Remove character if count is 0
            if s_cnt[s[i - p_len + 1]] == 0:
                del s_cnt[s[i - p_len + 1]]
        return output
