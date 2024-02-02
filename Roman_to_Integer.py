# https://leetcode.com/problems/roman-to-integer/description/
# Given a Roman numeral, convert it to an integer.

# solved in 2 ways

class Solution:
    def romanToInt(self, s: str) -> int:
        # assigning Romans to numbers in a dictionary
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        # initializing variables
        sum = 0
        i = 0
        # storing length of the input string
        s_len = len(s)
        while i < s_len:
            # checking if the combination of Romans present in the string
            if i < s_len-1 and s[i]+s[i+1] in roman:
                # converting roman to integer
                sum += roman[s[i]+s[i+1]]
                # incrementing variable to skip the next character
                i+=1
            else:
                sum += roman[s[i]]
            i += 1
        return sum
      
#-------------------------------------------------------
# Alternate Solution
class Solution2:
    def romanToInt2(self, s: str) -> int:
        # assigning romans to numbers in a dictionary (IV = -2 because I,V are already extracted (I+V = 6) - (IV = 4 = 2)) similarly other values are calculated
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':-2,'IX':-2,'XL':-20,'XC':-20,'CD':-200,'CM':-200}
        sum = 0
        for k, v in roman.items(): 
            # calculate the sum for respective Roman numeral occurrences
            if k in s:
                sum += v*s.count(k)
        return sum  

