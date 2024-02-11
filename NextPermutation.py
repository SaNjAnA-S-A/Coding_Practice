# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        flag = 0
        for i in range(1,len(nums)):
            # checking if digits are in increasing order in reverse order and finding pivot index
            if nums[-i] > nums[-i-1]:
                flag = 1
                break
        # reverse list if list is in decreasing order
        if flag == 0:
            nums.reverse()
        else:
            # sort the elements after the pivot
            nums[-i:] = sorted(nums[-i:])
            for j in range(i):
                # swap the element that is next larger number to pivot
                if nums[-i-1] < nums[-i+j]:
                    nums[-i-1], nums[-i+j] = nums[-i+j], nums[-i-1]
                    break
        
        
