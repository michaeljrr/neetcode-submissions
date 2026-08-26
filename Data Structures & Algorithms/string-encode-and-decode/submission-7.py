class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append('#')
            encoded.append(s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        ls = []
        while i < len(s):
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            ls.append(s[j+1 : j+length+1])
            i = j + length + 1
            j = i
        return ls

        
                

