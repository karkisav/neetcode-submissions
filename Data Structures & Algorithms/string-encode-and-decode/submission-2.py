class Solution:

    def encode(self, strs: List[str]) -> str:
        string_e = ""
        for s in strs:
            string_e += str(len(s)) + "#" + s
        return string_e

    def decode(self, s: str) -> List[str]:
        strings_d = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            strings_d.append(s[i:j])
            i = j
        return strings_d