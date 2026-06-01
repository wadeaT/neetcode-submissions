class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapinS = {}
        
        for char in s:
            if char in mapinS:
                mapinS[char] +=1
            else: 
                mapinS[char] = 1
        
        for char in t:
            if char in mapinS:
                mapinS[char] -=1
                m = mapinS[char]
                if m < 0 :
                    return False
            else: 
                return False
        for char in mapinS:
            if mapinS[char] != 0 :
                return False
        return True