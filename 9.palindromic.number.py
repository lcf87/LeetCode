class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        temp = x
        digit = 0
        result = 0

        while temp > 0:
        	digit = temp % 10
        	temp /= 10
        	result *= 10
        	result += digit

        return result == x 
        
    
def main():
	s = Solution()
	s.isPalindrome(123211)
        
if __name__ == '__main__':
	main()