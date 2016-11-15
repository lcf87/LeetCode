def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    
    i = 0
    count = 1
    sub_string = ''
    string_length = len(s)


    while i + count <= string_length:
    	sub_string = s[i:i+count]

    	occurance = []
		
		for char in sub_string:
			occurance.append(char)

    	if len(occurance) != len(set(occurance)):
    		# duplicity occurred
    		i += 1
    	else:
    		count += 1

    return count - 1


def main():
	print lengthOfLongestSubstring('abcabcbb')

if __name__ == '__main__':
	main()