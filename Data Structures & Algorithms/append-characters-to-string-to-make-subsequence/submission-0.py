class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0

        lenT = len(t)
        lenS = len(s)
        while (i<lenS and j<lenT):
            if s[i] == t[j]:
                j +=1
            i +=1

        return lenT-j

