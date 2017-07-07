class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        cons_table = [0 for i in range(len(s))]
        for index, i in enumerate(s):
            if i == "(":
                stack.append((index, i))
            elif i == ")":
                if not stack or (stack[-1][1] != "("):
                    stack = []
                else:
                    start_index = stack.pop()[0]
                    curr_fit = index - start_index + 1
                    curr_fit += cons_table[start_index - 1]
                    cons_table[index] = curr_fit
        return max(cons_table) if cons_table else 0


a = Solution()
print (a.longestValidParentheses("()"))
