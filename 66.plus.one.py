class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        Given a non-negative number represented as an array of digits, plus one to the number.

		The digits are stored such that the most significant digit is at the head of the list.
        """
        i = len(digits) - 1
        carry = 1

        while i >= 0:
        	if (digits[i] + carry >= 10):
        		carry = 1
        		digits[i] = 0
        	else:
        		
        		digits[i] += carry
        		carry = 0
        	i -= 1

        if digits[0] == 0:
        	digits.insert(0, 1)
        return digits

if __name__ == '__main__':
	print Solution().plusOne([1,9,9])

