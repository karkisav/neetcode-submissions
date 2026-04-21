class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        upper_bound = max(piles)
        lower_bound = 1

        def calc_hours(piles, speed):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours
        res = 0
        while lower_bound <= upper_bound:
            mid = lower_bound + (upper_bound - lower_bound) // 2
            if calc_hours(piles, mid) <= h:
                res = mid
                upper_bound = mid - 1
            else:
                lower_bound = mid + 1
        return res
