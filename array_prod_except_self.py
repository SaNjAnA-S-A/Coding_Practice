class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        out = []
        if 0 not in nums:
            for i in nums:
                prod = prod * i
            for j in nums:
                out.append(int(prod/j))
        else:
            nums2 = list(filter(lambda num: num != 0, nums))
            if len(nums2) < len(nums)-1:
                out = [0] * len(nums)
            else:
                for i in nums2:
                    prod = prod * i
                for j in nums:
                    if j == 0:
                        out.append(int(prod))
                    else:
                        out.append(0)
        return out