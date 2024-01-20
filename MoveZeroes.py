# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                print(nums[i],nums[j])
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
