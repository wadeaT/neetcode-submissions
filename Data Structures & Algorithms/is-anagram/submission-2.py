class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapin = {}
        n = len(s)
        if n != len(t):
            return False
        
        for i in range(0,n):
            if s[i] in mapin:
                mapin[s[i]] +=1
            else:
                mapin[s[i]] = 1
            if t[i] in mapin:
                mapin[t[i]] -=1
            else: 
                mapin[t[i]] = -1

        for char in mapin:
            if mapin[char] != 0:
                return False
        return True