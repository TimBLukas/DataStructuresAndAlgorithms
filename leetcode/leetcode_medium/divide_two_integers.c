/**
 * Leetcode 29: Divide Two Integers
 *
 * Given two integers dividend and divisor, divide two integers without using
 * multiplication, division, and mod operator.
 *
 * The integer division should truncate toward zero, which means losing its
 * fractional part. For example, 8.345 would be truncated to 8, and -2.7335
 * would be truncated to -2.
 *
 * Return the quotient after dividing dividend by divisor.
 *
 * Note: Assume we are dealing with an environment that could only store
 * integers within the 32-bit signed integer range: [−231, 231 − 1]. For this
 * problem, if the quotient is strictly greater than 231 - 1, then return 231 -
 * 1, and if the quotient is strictly less than -231, then return -231.
 */

int divide(int dividend, int divisor) {
    long long dvd = dividend;
    long long dvs = divisor;

    int negative = (dvd < 0) != (dvs < 0);

    dvd = dvd < 0 ? -dvd : dvd;
    dvs = dvs < 0 ? -dvs : dvs;

    long long result = 0;

    while (dvd >= dvs) {
        long long value = dvs;
        long long multiple = 1;

        while (value + value <= dvd) {
            value += value;
            multiple += multiple;
        }

        dvd -= value;
        result += multiple;
    }

    if (negative)
        result = -result;

    if (result > 2147483647)
        return 2147483647;

    if (result < -2147483648LL)
        return -2147483648LL;

    return (int)result;
}
