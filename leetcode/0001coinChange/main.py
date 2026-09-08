def coinChange(self, coins: List[int], amount: int) -> int:
    coins_copy = coins.copy()
    amount_temp = amount
    coins_copy.sort()
    change = []
    while (amount_temp > 0):
        if (len(coins_copy) == 0):
            break
        if (coins_copy[-1] <= amount_temp):
            change.append(coins_copy[-1])
            amount_temp -= coins_copy[-1]
        else:
            coins_copy.pop()

    print(change)
    if (amount_temp == 0):
        return len(change)
    return -1






