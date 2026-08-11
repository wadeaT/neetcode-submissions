class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        sort = {}
        index = 0
        for char in order: 
            sort[char] = index
            index +=1
        
        freq = {}
        for char in s:
            if char in freq:
                freq[char] +=1
            else:
                freq[char] = 1
        res =""
        for char in sort:
            if char in freq:
                res += char * freq[char]
            
        for char in freq:
            if char not in sort:
                res += char * freq[char]

        return res    
