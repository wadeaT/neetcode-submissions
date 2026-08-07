class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""
        j = 0
        char = ""
        while True:
            if len(strs[0]) <= j:
                return prefix
            char = strs[0][j]
            for i in range(len(strs)):
                if len(strs[i]) <= j or char != strs[i][j]:
                    return prefix
            j+=1 
            prefix += char
        return prefix