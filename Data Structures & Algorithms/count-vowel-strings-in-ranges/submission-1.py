class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowels = {"a","e","i","o","u"}
        prefix = []
        sum_ = 0

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                sum_ +=1
            prefix.append(sum_)
        
        ans = []
        
        for query in queries: 
            right = prefix[query[1]]
            left = prefix[query[0]-1] if query[0] > 0 else 0
            ans.append( right - left)
        
        return ans