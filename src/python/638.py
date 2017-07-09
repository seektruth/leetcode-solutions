import copy


class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """

        def l_add(a, b):
            return [i + j for i, j in zip(a, b)]

        def fit(l):
            brought = reduce(l_add, [special[i] for i in l])
            for i in range(len(needs)):
                if brought[i] > needs[i]:
                    return False
            return True

        def pay(scheme):
            brought = reduce(l_add, [special[i] for i in scheme])
            paid = brought[-1]
            for i in range(len(needs)):
                paid += (needs[i] - brought[i]) * price[i]
            return paid

        min_pay = 0
        for i in range(len(needs)):
            min_pay += needs[i] * price[i]
        visited = set()
        q = filter(fit, [[i] for i in range(len(special))])
        while q:
            scheme = q.pop()
            scheme_paid = pay(scheme)
            if scheme_paid < min_pay:
                min_pay = scheme_paid
            for i in range(len(special)):
                n_scheme = copy.copy(scheme)
                n_scheme.append(i)
                key = ''.join([str(i) for i in sorted(n_scheme)])
                if key not in visited:
                    visited.add(key)
                    if fit(n_scheme):
                        q.append(n_scheme)
        return min_pay


a = Solution()
print a.shoppingOffers([0,0,0],[[1,1,0,4],[2,2,1,9]],[1,1,1])

