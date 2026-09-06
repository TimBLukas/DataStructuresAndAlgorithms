"""
Leetcode 3971: Maximum Total Value

You are given two integer arrays value and decay, and an integer m.
- value[i] represents the initial value at index i.
- decay[i] represents how much the value decreases after each selection of index i.

You may select any index multiple times. The total number of selections across all indices must not exceed m.
If you select index i for the tth time, where t is 1-indexed, the value gained is value[i] - decay[i] * (t - 1).

Return the maximum total value you can obtain. Since the answer may be large, return it modulo 109 + 7.
"""


class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:
        MOD = 10**9 + 7
        positive_count = 0

        for v, d in zip(value, decay):
            positive_count += (v - 1) // d + 1

        m = min(m, positive_count)

        def count_at_least(x):
            count = 0

            for v, d in zip(value, decay):
                if v >= x:
                    count += (v - x) // d + 1
                    if count >= m:
                        return count
            return count

        lo, hi = 1, max(value)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if count_at_least(mid) >= m:
                lo = mid
            else:
                hi = mid - 1
        x = lo

        total, count = 0, 0

        for v, d in zip(value, decay):
            if v >= x:
                k = (v - x) // d + 1

                total += k * (2 * v - (k - 1) * d) // 2
                count += k

        total -= (count - m) * x
        return total % MOD


if __name__ == "__main__":
    value = [5, 4]
    decay = [1, 1]
    m = 3
    print(Solution().maxTotalValue(value, decay, m))
    value = [10, 1]
    decay = [10, 1]
    m = 3
    print(Solution().maxTotalValue(value, decay, m))
