class Pathfinder:
    @staticmethod
    def naive(pos_y=0, pos_x=0, board_height=3, board_width=3):
        if pos_y == board_height - 1 and pos_x == board_width - 1:
            return 1

        if pos_y >= board_height or pos_x >= board_width:
            return 0

        down = Pathfinder.naive(pos_y + 1, pos_x, board_height, board_width)
        right = Pathfinder.naive(pos_y, pos_x + 1, board_height, board_width)
        total = down + right
        return total

    @staticmethod
    def memoized(
        pos_y=0, pos_x=0, board_height=3, board_width=3,
        cache=None, debug=False
    ):
        if cache is None:
            cache = {}

        key = (pos_y, pos_x)

        if key in cache:
            if debug:
                print(f"cache hit: {key} -> {cache[key]}")
            return cache[key]

        if pos_y == board_height - 1 and pos_x == board_width - 1:
            cache[key] = 1
            return 1

        if pos_y >= board_height or pos_x >= board_width:
            cache[key] = 0
            return 0

        down = Pathfinder.memoized(
            pos_y + 1, pos_x, board_height, board_width, cache, debug
        )
        right = Pathfinder.memoized(
            pos_y, pos_x + 1, board_height, board_width, cache, debug
        )
        total = down + right

        cache[key] = total
        if debug:
            print(f"store: {key} -> {total}")
        return total

    @staticmethod
    def tabulated(board_height=3, board_width=3):
        dp = [[0 for _ in range(board_width)] for _ in range(board_height)]

        dp[0][0] = 1

        for x in range(0, board_width):
            dp[0][x] = 1

        for y in range(0, board_height):
            dp[y][0] = 1

        for y in range(1, board_height):
            for x in range(1, board_width):
                dp[y][x] = dp[y - 1][x] + dp[y][x - 1]

        return dp[board_height - 1][board_width - 1]

    @staticmethod
    def rolling_window(board_height=3, board_width=3):
        prev_row = [1] * board_width

        for y in range(1, board_height):
            curr_row = [1] * board_width
            for x in range(1, board_width):
                curr_row[x] = curr_row[x - 1] + prev_row[x]
            prev_row = curr_row

        return prev_row[board_width - 1]


# Przykład użycia dla gridu 3x3 Naive
board_height, board_width = 3, 3
result = Pathfinder.naive(0, 0, board_height, board_width)
print("\nFINAL RESULT =", result)

# Przykład użycia dla gridu 3x3 Memoized
board_height, board_width = 3, 3
result = Pathfinder.memoized(0, 0, board_height, board_width)
print("\nFINAL RESULT =", result)

# Przykład użycia dla gridu 3x3 Tabulated
board_height, board_width = 3, 3
result = Pathfinder.tabulated(board_height, board_width)
print("\nFINAL RESULT =", result)

# Przykład użycia dla gridu 3x3 Rolling Window
board_height, board_width = 6, 6
result = Pathfinder.rolling_window(board_height, board_width)
print("\nFINAL RESULT =", result)
