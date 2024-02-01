"""https://leetcode.com/problems/reverse-string/description/
#Write a function that reverses a string. The input string is given as an array of characters.
#You must do this by modifying the input array in-place with O(1) extra memory.
# Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        r = len(s)-1
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[r-i]
            s[r-i] = temp
