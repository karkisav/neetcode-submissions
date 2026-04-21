class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Count_s = {key: 0 for key in s}
        Count_t = {key: 0 for key in t}
        letter = 0
        for letter in s:
            Count_s[letter] +=1
        letter = 0
        for letter in t:
            Count_t[letter] +=1

        if Count_s == Count_t:
            return True
        return False