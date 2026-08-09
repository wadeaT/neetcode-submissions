class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashtable = {}

        # number value char - a + 1

        for word in strs:
            hashcode = 0
            sortedWord = "".join(sorted(word))
            for i in range(len(sortedWord)):
                hashcode += (ord(sortedWord[i])-ord("a")+1) * (31**i)
            if hashcode not in hashtable:
                hashtable[hashcode] = []
            hashtable[hashcode].append(word)
        
        return list(hashtable.values())
