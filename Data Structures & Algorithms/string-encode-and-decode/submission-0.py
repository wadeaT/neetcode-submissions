class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for word in strs:
            for char in word:
                encoded_str += f"{ord(char)},"
            encoded_str += ("_")
        return encoded_str
    
    def decode(self, s: str) -> List[str]:
        lst = []
        character_number = ""
        word = ""
        

        n = len(s)
        i = 0
        while i < n:
            if s[i] != "," and s[i] != "_":
                character_number +=s[i]
            else:
                if s[i] == ",":
                    word += chr(int(character_number))
                    character_number = ""
                else:
                    lst.append(word)
                    word = ""
            i+=1 
        return lst