class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            arranged = sorted(word)
            arranged = ''.join(arranged)
            if arranged not in seen:
                seen[arranged] = []
            seen[arranged].append(word)
        return list(seen.values())