import operator


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words: return []
        l = len(words[0])
        l2 = len(words)
        table = {}
        table2 = []
        table3 = []
        for index, word in enumerate(words):
            table[word] = index + 1
        for i in range(0, len(s) - l + 1):
            t = s[i:i + l]
            v = table.get(t, -1)
            table2.append(v)
        for i in range(len(table2) - (l2 - 1) * l ):
            h = reduce(operator.add, table2[i:i+l * (l2 - 1) + 1:l], 0)
            table3.append((i, h))
        hash_sum = reduce(lambda a,b: a + table[b], words, 0)
        table3 = filter(lambda x: x[1] == hash_sum, table3)
        return list(map(lambda x: x[0], table3))

a = Solution()
print(a.findSubstring("aaa", ["a","a"]))


