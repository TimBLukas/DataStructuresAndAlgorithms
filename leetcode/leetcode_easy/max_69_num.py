"""
1323: Maximum 69 Number

You are given a positive integer `num` consisting only of digits `6` and `9`
Return the maximum number you can get by changing at most one digit (6 becomes 9 and 9 becomes 6)
"""

class Solution:
        def maximum69Number (self, num: int) -> int:
                num_str = str(num)
                return_val = ""
                for c in num_str:
                        if c == '6':
                                return_val += "9"
                                break
                        else:
                                return_val += c
                        
                return_val += "" if len(return_val) == len(num_str) else num_str[-1 * (len(num_str) - len(return_val)):]
                return int(return_val)
