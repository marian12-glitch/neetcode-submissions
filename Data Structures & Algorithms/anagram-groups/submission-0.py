class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for char in strs:
            K_word = "".join(sorted(char))
            
            
            if K_word not in seen:
                seen[K_word] = [char]

            else:
                seen[K_word].append(char)

        return list(seen.values())
