class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            difference = target - nums[i]

            if d.get(difference) is not None:
                return [d[difference],i]
            else: d.update({nums[i] : i})