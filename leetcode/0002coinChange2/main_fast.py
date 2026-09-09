class Solution:
    # this is too slow... interesting...
    def change(self, amount: int, coins: List[int]) -> int:
        a = amount
        c = coins.copy()
        c.sort()
        dp = dict()
        def changeTemp(a, i):
            # assume that we return the number of zeros in the nodes
            # in the case that we get to the root node
            if (a, i) in dp:
                return dp[(a, i)]
            if a == 0:
                return 1
            elif a < 0 or i < 0:
                return 0
            # memoize it
            dp[(a, i)] = changeTemp(a - c[i], i) + changeTemp(a, i - 1)
            return dp[(a, i)]
        return changeTemp(amount, len(c) - 1)
