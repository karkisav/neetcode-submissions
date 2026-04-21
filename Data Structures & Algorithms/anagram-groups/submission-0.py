class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Anagrams = []
        Same_ana = {}

        for str1 in strs:
            sorted_str = ''.join(sorted(str1))
            if sorted_str not in Same_ana:
                Same_ana[sorted_str] = []
            Same_ana[sorted_str].append(str1)

        for values in Same_ana.values():
            Anagrams.append(values)

        return Anagrams