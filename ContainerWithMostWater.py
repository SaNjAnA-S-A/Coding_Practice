# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initialize variables
        width = len(height)-1
        water = 0
        m = 0
        n = width
        for i in range(0,width):  
            # set two pointers at each end of array to get max water stored
            if height[m] < height[n]:
                # calculate water stored and compare it with previous values
                if height[m] * width > water:
                    water = height[m] * width
                # Increment the pointer at smaller pillar
                m += 1
            else:
                if height[n] * width > water:
                    water = height[n] * width
                # Increment the pointer at smaller pillar
                n -= 1
            width -=1
        return water
        
