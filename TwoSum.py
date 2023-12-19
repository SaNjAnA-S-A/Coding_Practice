class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = []
        for i in range(len(nums)):
            curr = nums[i]
            num = target - curr
            if num in store:
                return [i,store.index(num)]
            store.append(curr)
        
