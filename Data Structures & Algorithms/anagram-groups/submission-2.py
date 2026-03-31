
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for i in range(len(strs)):
            unicode = 0
            for letter in strs[i]:
                unicode += ord(letter) ** 2
            

            d[unicode].append(strs[i])

                
        return list(d.values())
