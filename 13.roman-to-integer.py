#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        stack = []
        total = 0
        #what we should keep in mind is that the roman numbers are made such that each value that is right to the other one like this "MD" D<M the time where the left is inferior the right means that we need to substract that number like this "IV" we have I <V yet to it s left so we need to have V-I and that what we are doing each time a value to the left is less than the one on the right we substract it from the total and we just append the new one , and that way we account for the special cases 
        for c in s:
            value = roman_to_int[c]
            if not stack or value <= stack[-1]:
                stack.append(value)
            else:
                while stack and value > stack[-1]:
                    prev_value = stack.pop()
                    total -= prev_value
                stack.append(value)

        return total +sum(stack)
# @lc code=end

