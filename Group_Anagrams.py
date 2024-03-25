#https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for word in strs:
            # initialise a list with 26 0's representing each alphabet count
            op_keys = [0] * 26
            # for each letter in the word, increment the alphabet count in the list
            for char in word:
                op_keys[ord(char) - ord('a')] += 1
            # store the list as key and the word as value in the dictionary 
            output[tuple(op_keys)].append(word)
        return output.values()
