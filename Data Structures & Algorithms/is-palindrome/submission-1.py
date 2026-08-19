class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Two pointers 

        i = 0 
        j = len(s) -1 

        def valid(char: str):
            value = ord(char)
            if value >= ord("a") and value <= ord("z"):
                return True
            elif value >= ord("0") and value <= ord("9"):
                return True
            return False
        
        s = s.lower()
        while (i <= j ):
            if valid(s[i]):
                if valid(s[j]):
                    if s[i] != s[j]:
                        return False
                    else:
                        i+=1 
                        j-=1
                else:
                    j -= 1
            else:
                i+=1
        return True