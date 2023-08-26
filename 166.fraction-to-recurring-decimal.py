#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        result = []
        if numerator < 0 and denominator > 0 or numerator >= 0 and denominator < 0:
            result.append('-')
        
        numerator, denominator = abs(numerator), abs(denominator)
        
        result.append(str(numerator // denominator))
        
        remainder = numerator % denominator
        
        if remainder == 0: 
            return ''.join(result) #case where the division has no remainder 2/1 for example

        result.append('.') #we are sure there is a remainder so we add a .

        d = {}
        '''
        A dictionary d is used to keep track of remainders and their corresponding positions in the result. This is crucial for identifying where the repeating part begins if there is a repeating decimal.

A loop starts where the remainder is not zero. The loop performs long division steps by multiplying the remainder by 10 and appending the integer division result (remainder // denominator) to the result.

The new remainder is updated as remainder % denominator.

If the new remainder is already present in the dictionary d, it means that the division process has encountered this remainder before. This implies that a repeating decimal pattern is starting. In this case, the code inserts an opening parenthesis '(' at the position where the repeating part starts and adds a closing parenthesis ')' at the end of the result to enclose the repeating part.

If the new remainder is not in the dictionary, its current position in the result is stored in the dictionary d.

The loop continues until the remainder becomes zero, which means the division is complete.

Finally, the code joins the list of characters in the result list to create the final decimal representation of the fraction, including any repeating decimal parts enclosed in parentheses.
        '''
        while remainder != 0:

            if remainder in d:

                result.insert(d[remainder], '(')
                result.append(')')

                return ''.join(result)
            
            d[remainder] = len(result)
            
            remainder *= 10
            result += str(remainder // denominator)
            remainder = remainder % denominator
        
        return ''.join(result)

# @lc code=end

