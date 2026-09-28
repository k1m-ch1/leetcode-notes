class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def comparator(a, b):
            res = int(str(b) + str(a)) - int(str(a) + str(b))
            if res < 0:
                return -1
            elif res > 0:
                return 1
            return 0
        from functools import cmp_to_key, reduce
        as_list = sorted(nums, key=cmp_to_key(comparator))
        as_str_list = [str(n) for n in as_list]
        return str(int(reduce(lambda a, b: a + b, as_str_list)))

