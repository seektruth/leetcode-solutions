class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=len)
        prefix = strs[0] if strs else ""
        for s in strs:
            i = 0
            while i < len(prefix):
                if prefix[i] == s[i]:
                    i += 1
                else:
                    break
            prefix = prefix[0:i]
        return prefix

a = Solution()
print a.longestCommonPrefix(["a", "aaa", "aa", "b"])