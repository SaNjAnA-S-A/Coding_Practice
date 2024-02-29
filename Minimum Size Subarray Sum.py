# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        m,summ,flag = 0,0,0
        count, min_count = 0, float('inf')
        if target in nums:
            return 1
        for i in range(len(nums)):
            summ += nums[i]
            count += 1
            while summ >= target:
                summ -= nums[m]
                m += 1
                count -=1
                flag = 1
            if count < min_count and flag == 1:
                min_count = count + 1
            flag = 0
        return min_count if min_count!= float('inf') else 0
