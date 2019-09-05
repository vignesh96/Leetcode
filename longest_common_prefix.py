class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        zipped_strs = list(zip(*strs))
        prefix = ""
        for tup in zipped_strs:
            if len(set(tup)) == 1:
                prefix += tup[0]
            else:
                break
        return prefix
