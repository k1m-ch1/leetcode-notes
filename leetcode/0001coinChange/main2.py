
def coinChange(self, coins: List[int], amount: int) -> int:
    coins_copy = coins.copy()
    amount_temp = amount
    coins_copy.sort(reverse=True)
    dp = dict()
    # suppose that I already know the solution to a smaller problem, and it's stored in dp
    def coinChangeTemp(amount: int) -> int:
        if amount in dp:
            return dp[amount]
        if amount <= 0:
            return 0
        temp_number_of_coins = []
        for coin in coins:
            if amount == coin:
                return 1
            elif amount > coin:
                # try to move down a path
                coinsBelow = coinChangeTemp(amount - coin)
                if coinsBelow < 0:
                    # if that path is dead, then continue
                    continue
                # this should be safe
                temp_number_of_coins.append(1 + coinsBelow)
        if len(temp_number_of_coins) == 0:
            # if the path is dead, mark it as dead by placing -1
            dp[amount] = -1
            return -1
        else:
            dp[amount] = min(temp_number_of_coins)
            return dp[amount]
    return coinChangeTemp(amount)
