class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ...
        """make a hash data structure which keeps a track of the count
        TODO: If the hash has any count 1 then its true, 
        i.e its got duplicated"""

        #initialize a hash named count
        Count = {key: 0 for key in nums}
        for num in nums:
            if Count[num] >= 1:
                return True
            else: Count[num] += 1
        return False