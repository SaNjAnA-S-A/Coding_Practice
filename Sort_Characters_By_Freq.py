# https://leetcode.com/problems/sort-characters-by-frequency/
""" Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them."""

class Solution:
    def frequencySort(self, s: str) -> str:
        # initialize the output string
        output=""
        # store the counter of each character in decreasing order
        freq = Counter(s).most_common()
        for i in freq:
            # obtain output by appending the character occurrences in decreasing order
            output += i[0]*i[1]
        return output
