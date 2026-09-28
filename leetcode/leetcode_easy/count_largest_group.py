"""
Leetcode 1399: Count Largest Group

We need to group the numbers from 1 to n according to the sum of its digits.
For example, the numbers 14 and 5 belong to the same group, whereas 13 and 3 belong to different groups.

Return the number of groups that have the largest size, i.e. the maximum number of elements.
"""


from collections import Counter

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def calc_digit_sum(n: int) -> int:
            return sum([int(i) for i in str(n)])
        digit_sums = []
        for i in range(1, n+1):
            ds = calc_digit_sum(i)
            digit_sums.append(ds)

        print(sorted(digit_sums))
        c = Counter(digit_sums)        
        max_count = None
        cnt = 0
        for ds, count in c.most_common():
            if max_count is None:
                max_count = count
                cnt = 1
            else:
                if count != max_count:
                    return cnt
                else:
                    cnt += 1
        return cnt