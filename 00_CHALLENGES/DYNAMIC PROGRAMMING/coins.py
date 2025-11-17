import time


class Coins:

    @staticmethod
    def recursive(coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        return 1 + min(
            (Coins.recursive(coins, amount - c) for c in coins
             if c <= amount),
            default=float('inf')
        )

    @staticmethod
    def memoized(coins, amount, cache=None):
        if cache is None:
            cache = {}
        if amount in cache:
            return cache[amount]
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        best = min(
            (Coins.memoized(coins, amount - c, cache)
                for c in coins if c <= amount), default=float('inf')
        )
        cache[amount] = 1 + best
        return cache[amount]

    @staticmethod
    def tabulated(coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != float('inf') else -1


# Sprawdzenie działania i czasów wykonania poszczególnych metod \
# dla Coins [1,2,3] i amount = 5

# Coins Recursive
time_start = time.time()
print(f' Minimum Movements to get 5 using coins [1, 2, 3]: \
      {Coins.recursive([1, 2, 3], 5)}')
time_end = time.time()
print("Recursive Execution time:", time_end - time_start)

# Coins Memoized
time_start = time.time()
print(f' Minimum Movements to get 5 using coins [1, 2, 3]: \
       {Coins.memoized([1, 2, 3], 5)}')
time_end = time.time()
print("Memoized Execution time:", time_end - time_start)

# Coins Tabulated
time_start = time.time()
print(f' Minimum Movements to get 5 using coins [1, 2, 3]: \
      {Coins.tabulated([1, 2, 3], 5)}')
time_end = time.time()
print("Tabulated Execution time:", time_end - time_start)
