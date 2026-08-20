class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        OpenParantheses = {"(", "{","["}
        CloseParantheses = {")":"(","}":"{", "]":"["}
        for i in range(len(s)):
            if s[i] in OpenParantheses:
                stack.append(s[i])
            else:
                if i> 0 and stack and CloseParantheses[s[i]] == stack[-1]:
                    stack.pop()
                else: 
                    return False
        
        return len(stack) == 0