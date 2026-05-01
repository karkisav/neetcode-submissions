class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqS1 = {}

        if len(s1) > len(s2):
            return False

        for c in s1:
            freqS1[c] = 1 + freqS1.get(c, 0)

        l, r = 0, len(s1) - 1

        while r < len(s2):
            freqS2 = {}
            for c in range(l, l + len(s1)):
                freqS2[s2[c]] = 1 + freqS2.get(s2[c], 0)
            
            if freqS1 == freqS2:
                return True
            else:
                l += 1
                r += 1
        
        return False