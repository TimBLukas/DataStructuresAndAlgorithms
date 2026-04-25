# Leetcode Nr. 88 - Merge Sorted Array
#


# Given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers ma and n, representing
# the numbers of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final arrray does not have to be returned, the final array with all elements is supposed to be nums1


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        # For Testing the function is modified to return the nums1 Array
        # For the solution the return type has to be None and the return statement has to be removed
        l_p, r_p = 0, 0

        while l_p <= m and r_p <= n:
            idx = l_p + r_p

            if l_p == m:
                nums1[idx:] = nums2[r_p:]
                break

            elif r_p == n:
                break

            elif nums1[idx] <= nums2[r_p]:
                l_p += 1

            else:
                nums1.insert(idx, nums2[r_p])
                nums1.pop()
                r_p += 1

        return nums1


class Tester:
    # For Testing the function has to be changed to return nums1
    def test1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        result = Solution().merge(nums1, m, nums2, n)

        assert result == [1, 2, 2, 3, 5, 6], f"The result was {result}"
        print(f"The result was: {result}")

    def test2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0

        result = Solution().merge(nums1, m, nums2, n)

        assert result == [1], f"The result was {result}"
        print(f"The result was: {result}")

    def run_tests(self):
        print("Running Tests")
        self.test1()
        self.test2()

        print("Tests Completed")


if __name__ == "__main__":
    tester = Tester()

    tester.run_tests()
