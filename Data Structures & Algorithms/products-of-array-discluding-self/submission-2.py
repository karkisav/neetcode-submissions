class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        suffix = []
        prefix = []
        result = []

        suf = 1
        pre = 1
        n = len(nums)

        for i in range(n):
            if i == 0:
                prefix.append(1)
            else:
                pre *= nums[i - 1]
                prefix.append(pre)

        for i in range(n - 1, -1, -1):
            if i == n - 1:
                suffix.append(1)
            else:
                suf *= nums[i + 1]
                suffix.append(suf)
            result.append(suffix[n - i - 1] * prefix[i])

        return result[::-1]