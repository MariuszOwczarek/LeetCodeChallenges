import time


class Fibonacci:
    # Metoda podstawowa - rekurencyjna
    @staticmethod
    def recursive(fib_num):
        if fib_num == 0:
            return 0
        if fib_num == 1:
            return 1
        return (Fibonacci.recursive(fib_num - 2) +
                Fibonacci.recursive(fib_num - 1))

    # Metoda z memoizacją - cache w argumencie funkcji
    @staticmethod
    def memoized(fib_num, cache={0: 0, 1: 1}):
        if fib_num in cache:
            return cache[fib_num]
        else:
            cache[fib_num] = (Fibonacci.memoized(fib_num - 2) +
                              Fibonacci.memoized(fib_num - 1))
        return cache[fib_num]

    # Metoda z memoizacją - oddzielny cache
    @staticmethod
    def memoized_separate_cache(n):
        cache = {0: 0, 1: 1}
        return Fibonacci._memo(n, cache)

    @staticmethod
    def _memo(n, cache):
        if n in cache:
            return cache[n]
        cache[n] = (Fibonacci._memo(n - 1, cache) +
                    Fibonacci._memo(n - 2, cache))
        return cache[n]

    # Metoda tabulacyjna - bottom-up
    @staticmethod
    def tabulated(fib_num):
        dp = [0] * (fib_num + 1)
        dp[0] = 0
        dp[1] = 1

        if fib_num == 0:
            return 0
        if fib_num == 1:
            return 1
        for i in range(2, fib_num + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[fib_num]

    # Metoda z oknem przesuwanym - rolling window
    @staticmethod
    def rolling_window(fib_num):
        if fib_num == 0:
            return 0
        if fib_num == 1:
            return 1
        prev_2 = 0
        prev_1 = 1

        for i in range(2, fib_num + 1):
            curr = prev_2 + prev_1
            prev_2 = prev_1
            prev_1 = curr
        return prev_1


# Sprawdzenie działania i czasów wykonania poszczególnych metod doa Fib(20)
# Fibonacci Recursive
time_start = time.time()
Fibonacci.recursive(20)
time_end = time.time()
print("Recursive Execution time:", time_end - time_start)

# Fibonacci Memoized
time_start = time.time()
Fibonacci.memoized(20)
time_end = time.time()
print("Memoized Execution time:", time_end - time_start)

# Fibonacci Memoized with separate Cash
time_start = time.time()
Fibonacci.memoized_separate_cache(20)
time_end = time.time()
print("Memoized Separate Cache Execution time:", time_end - time_start)

# Fibonacci Tabulated
time_start = time.time()
Fibonacci.tabulated(20)
time_end = time.time()
print("Tabulated Execution time:", time_end - time_start)

# Fibonacci Windowed
time_start = time.time()
Fibonacci.rolling_window(20)
time_end = time.time()
print("Rolling Window Execution time:", time_end - time_start)
