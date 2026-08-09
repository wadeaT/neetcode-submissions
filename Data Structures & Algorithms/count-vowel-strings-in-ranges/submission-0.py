class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #brute force
        vowels = {"a","e","i","o","u"}
        arr = []
        for query in queries: 
            sumVowels = 0
            for i in range(query[0],query[1]+1):
                if (words[i][0] in vowels) and (words[i][-1] in vowels):
                    sumVowels +=1
            arr.append(sumVowels)
        return arr