class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while (i <= j):
            idx = int((i + j) / 2)
            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                i =  idx + 1
            elif nums[idx] > target:
                j = idx - 1
        return -1