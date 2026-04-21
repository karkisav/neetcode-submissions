class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        Sums = []
        nums.sort()

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, len(nums) - 1
            val = -nums[i]
            while(j < k):
                if val == nums[j] + nums[k]:
                    Sums.append([-val,nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                if val > nums[j] + nums[k]:
                    j += 1
                if val < nums[j] + nums[k]:
                    k -= 1
        return Sums