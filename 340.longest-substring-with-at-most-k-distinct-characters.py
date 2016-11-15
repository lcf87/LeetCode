class Solution(object):
    def substring(self, string, k):
        """
        Given a string, find the length of the longest substring T that contains at most k distinct characters.
        For example, given s = 'eceba' and k = 2,
        T is "ece" which its length is 3.
        """
        
        # sliding window solution?
        count = k   # at least 2 letters to form the string
        i = 0       # start from the beginning
        sbs = ''    # substring of length count

        while i + count <= len(string):
            sbs = string[i:i+count]

            distinct = ''.join(set(sbs))

            if len(distinct) > k:
                i += 1
            else:
                count += 1

        return count-1




if __name__ == '__main__':
    print Solution().substring('ecebaa', 4)
