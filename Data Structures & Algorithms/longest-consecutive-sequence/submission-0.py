class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        L_hash = set()

        for num in nums:
            if num not in L_hash:
                L_hash.add(num)

        Candidates = set()

        for num in nums:
            if num - 1 not in L_hash:
                Candidates.add(num)

        # print(Candidates)
        Max = 0
        for Candidate in Candidates:
            temp = Candidate
            Count = 1
            while (temp + 1 in nums):
                Count += 1
                temp += 1
            Max = max(Max, Count)
        return Max
