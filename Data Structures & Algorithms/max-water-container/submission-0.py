class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        l, r = 0, len(heights) - 1

        while (l < r):
            val = (r - l) * min(heights[l], heights[r])
            water = max(water, val)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
        return water