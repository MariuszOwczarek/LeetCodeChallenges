import time


class ClimbingStairs:
    @staticmethod
    def recursive(steps):
        if steps == 1:
            return 1
        if steps == 2:
            return 2
        return (ClimbingStairs.recursive(steps - 1) +
                ClimbingStairs.recursive(steps - 2))

    @staticmethod
    def memoized(steps, cache={1: 1, 2: 2}):
        if steps in cache:
            return cache[steps]
        else:
            cache[steps] = (ClimbingStairs.memoized(steps - 1) +
                            ClimbingStairs.memoized(steps - 2))
        return cache[steps]

    @staticmethod
    def memoized_separate_cache(steps):
        cache = {1: 1, 2: 2}
        return ClimbingStairs._memo(steps, cache)

    @staticmethod
    def _memo(steps, cache):
        if steps in cache:
            return cache[steps]
        cache[steps] = (ClimbingStairs._memo(steps - 1, cache) +
                        ClimbingStairs._memo(steps - 2, cache))
        return cache[steps]

    @staticmethod
    def tabulated(steps):
        if steps == 1:
            return 1
        if steps == 2:
            return 2

        dp = [0] * (steps + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, steps + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[steps]

    @staticmethod
    def rolling_window(steps):
        if steps == 1:
            return 1
        if steps == 2:
            return 2

        prev2 = 1
        prev1 = 2

        for i in range(2, steps + 1):
            curr = prev2 + prev1
            prev2 = prev1
            prev1 = curr
        return prev1


# Sprawdzenie działania i czasów wykonania poszczególnych metod doa Fib(20)
# Climbing Stairs Recursive
time_start = time.time()
ClimbingStairs.recursive(20)
time_end = time.time()
print("Recursive Execution time:", time_end - time_start)

# Climbing Stairs Memoized
time_start = time.time()
ClimbingStairs.memoized(20)
time_end = time.time()
print("Memoized Execution time:", time_end - time_start)

# Climbing Stairs Memoized with separate Cash
time_start = time.time()
ClimbingStairs.memoized_separate_cache(20)
time_end = time.time()
print("Memoized with separate Cash Execution time:", time_end - time_start)

# ClimbingStairs Tabulated
time_start = time.time()
ClimbingStairs.tabulated(20)
time_end = time.time()
print("Tabulated Execution time:", time_end - time_start)

# ClimbingStairs Windowed
time_start = time.time()
ClimbingStairs.rolling_window(20)
time_end = time.time()
print("Rolling Window Execution time:", time_end - time_start)
