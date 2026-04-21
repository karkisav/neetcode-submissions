class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        PrevMap = {}

        for i, n in enumerate(nums):
            if (target - n) in PrevMap:
                return [PrevMap[target - n], i]
            PrevMap[n] = i
        return