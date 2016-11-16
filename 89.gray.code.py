import copy

""" 
The idea here is, on the most significant bit shift, like from 0010->0110,
only the MSB could toggle. That means, if we flip that bit already, then we 
can only repeat the order we followed before in a reversed order.

Say, 000 001 011 010 ------flipMSB----> 110 
From 110, notice the 10 part, to get all of its combinations, we can only follow 
the pattern back, like 10->11->01->00

"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        For example, given n = 2, return [0,1,3,2]. 
        """
        
    	# store the first 4 outcomes for 2 bits.
    	
    	if n == 0:
    		return [0]

    	table = [0, 1]

    	# total number of elements 
    	upper = 2 ** n

    	for i in xrange(2, n+1):
    		# make a copy of the list, and work on that
    		
    		new_table = copy.deepcopy(table)

    		# reverse it
    		new_table = new_table[::-1]

    		# add a msb to it
    		new_table = [num ^ (1 << (i-1)) for num in new_table]

    		table += new_table

    	return table

if __name__ == '__main__':
	print Solution().grayCode(1)

"""
SIMPLEST SOLUTION:
i^(i>>1)
"""