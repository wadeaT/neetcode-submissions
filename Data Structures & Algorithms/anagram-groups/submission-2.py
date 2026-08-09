class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}

        for word in strs:
            arr = [0]*26
            for char in word:
                arr[ord(char)-ord("a")] +=1
            
            key = tuple(arr)
            if key not in hashtable:
                hashtable[key] = []
            
            hashtable[key].append(word)
        
        return list(hashtable.values())