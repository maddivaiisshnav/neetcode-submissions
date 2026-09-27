class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (0,len(nums)):
            b = target - nums[i]
            for j in range(0,len(nums)):
                if nums[j]==b and i !=j:
                    return [i,j]


        