from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n):
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, prev2, prev1, length):
                if pos == m:
                    return (1, 0)  # (count of numbers, total waviness)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            10,  # sentinel
                            10,  # sentinel
                            0
                        )
                        total_count += cnt
                        total_waviness += wav

                    else:
                        if length >= 2:
                            add = int(
                                (prev2 < prev1 > d) or
                                (prev2 > prev1 < d)
                            )
                        else:
                            add = 0

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            prev1 if length >= 1 else 10,
                            d,
                            length + 1
                        )

                        total_count += cnt
                        total_waviness += wav + add * cnt

                return total_count, total_waviness

            return dp(0, True, False, 10, 10, 0)[1]

        return solve(num2) - solve(num1 - 1)