class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        class Node(object):
            def __init__(self, number):
                self.id = number
                self.next_node = []
                self.in_degree = 0

        table = [Node(i) for i in range(numCourses)]
        for node, pre in prerequisites:
            table[pre].next_node.append(table[node])
            table[node].in_degree += 1

        def find_course():
            for i, node in enumerate(table):
                if node.in_degree is 0:
                    return i
            else:
                return None

        while table:
            i = find_course()
            if i is None: return False
            for next_node in table[i].next_node:
                next_node.in_degree -= 1
            del table[i]

        return True

a = Solution()
print(a.canFinish(2,[[1, 0], [0, 1]]))