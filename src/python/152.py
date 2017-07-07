import operator


class Solution(object):
    def maxProduct(self, nums):
        num_str = ' '.join([str(x) for x in nums])
        nums_array = [[int(y) for y in x.split()] for x in num_str.split('0') if len(x.split()) > 0]
        if len(nums_array) is 0: return 0
        if len(nums_array) is 1 and len(nums_array[0]) is 1: return 0 if nums_array[0][0] < 0 and 0 in nums \
            else nums_array[0][0]

        def to_first_neg(num_array):
            for x in num_array:
                yield x
                if x < 0:
                    break

        def to_last_neg(num_array):
            return to_first_neg(reversed(num_array))

        def find_max_product(num_array):
            if len(num_array) is 1:
                return num_array[0]
            num_array = [int(x) for x in num_array]
            product = reduce(operator.mul, num_array)
            if product > 0: return product
            drop1 = to_first_neg(num_array)
            cons1 = reduce(operator.div, drop1, product)
            drop2 = to_last_neg(num_array)
            cons2 = reduce(operator.div, drop2, product)
            return max(cons1, cons2)

        return max(0, max(map(find_max_product, nums_array)))

a = Solution()
print(a.maxProduct([0, -2, 0]))

