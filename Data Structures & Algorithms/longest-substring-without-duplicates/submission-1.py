class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        hash_map = set()

        while r < len(s):
            if s[r] not in hash_map:
                hash_map.add(s[r])
                r += 1
            else:
                hash_map.remove(s[l])
                l += 1
            max_len = max(max_len, r - l)

        return max_len