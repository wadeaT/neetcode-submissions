class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n!=m:
            return False

        table = [0] * 26 

        for i in range(n):
            table[ord(s[i])-ord("a")] +=1 
            table[ord(t[i]) - ord("a")] -=1 
        
        for i in range(26):
            if table[i] != 0:
                return False
        return True
        