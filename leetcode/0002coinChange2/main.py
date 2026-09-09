class Solution:
    # this is too slow... interesting...
    def change(self, amount: int, coins: List[int]) -> int:
        a = amount
        c = coins.copy()
        c.sort()
        dp = dict()
        def changeTemp(a, lastCoinChange):
            # assume that we return the number of zeros in the nodes
            # in the case that we get to the root node
            if (a, lastCoinChange) in dp:
                return dp[(a, lastCoinChange)]
            if a == 0:
                return 1
            elif a < 0:
                return 0
            zeroAmounts = 0
            for coin in c:
                if coin > lastCoinChange:
                    # this ensures that we get rid of duplicates, because we only care about strictly decreasing case
                    break
                # memoize it
                zeroAmounts += changeTemp(a - coin, coin)

            # memoize it
            dp[(a, lastCoinChange)] = zeroAmounts
            return zeroAmounts
        return changeTemp(amount, max(c))
