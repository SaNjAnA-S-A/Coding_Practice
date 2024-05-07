# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        # the strinf is converted to list for further operations
        s = list(s)
        
        # iterate over the given string
        for i in range(len(s)):
            # push the index of '(' in the string to the stack
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                # pop the index of '(' from the stack if ')' is present as it is valid
                if stack:
                    stack.pop()
                # if ')' is present and no '(' in the valid form then remove ')' from string
                else:
                    s[i] = ''
        
        # Iterate over the stack and remove invalid ')' from the string by its index present in stack
        for i in stack:
            s[i] = ''
        return "".join(s)
