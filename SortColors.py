# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red,white,blue = 0,0,0
        # count number of red, white and blue objects
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
            else:
                blue += 1
        # Overwrite the array with the objects in respective counts
        nums.clear()
        nums += [0] * red + [1] * white + [2] * blue   
