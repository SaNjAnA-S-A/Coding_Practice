# https://leetcode.com/problems/longest-repeating-character-replacement/description/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len, m, max_count = 0,0,0
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            max_count = max(max_count, count[s[i]])
            if (i - m + 1) - max_count > k:
                count[s[m]] -= 1
                m += 1
            max_len  = max(max_count, i - m + 1)
        return max_len
