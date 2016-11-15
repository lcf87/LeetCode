class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
        	return ''

        # find the shortest string first
        shortest = strs[0]
        min_len = len(strs[0])

        for string in strs:
        	if (len(string) < min_len):
        		shortest = string
        		min_len = len(string)

        # try the shortest string first
        
        # stores matching for every string in the list
        res_arr = []
        found = False
        while min_len > 0 and found != True:
        	for string in strs:
        		if string[0:min_len] == shortest:
        			res_arr.append(1)
        		else:
        			res_arr.append(0)

        	# check if all matched
        	if (sum(res_arr) == len(strs)):
        		found = True
        	else:
        		res_arr = []
        		min_len -= 1
        		shortest = shortest[0:min_len]

        return shortest

if __name__ == '__main__':
	print Solution().longestCommonPrefix(['abcd', 'abd', 'abc'])