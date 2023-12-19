#https://leetcode.com/problems/buddy-strings/

from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            x = set(s)
            return len(x) < len(goal)
        arr = []
        match = 0
        if len(s) == len(goal):
            for c1, c2 in zip(s, goal):
                if c1 == c2:
                    match += 1
                else:
                    arr.append([c1,c2])
            if (len(s) - match) == 2:
                if arr[0][0] == arr[1][1] and arr[0][1] == arr[1][0]:
                    return True
        return False
