class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        convert = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

        # sliding 2 char window to check
        # first using 3 char window to check for XXX
        index = 0
        result = 0

        if (len(s) == 1):
            return convert[s[0]]

        while index + 2 < len(s):
            if (s[index] == s[index + 1] and s[index + 1] == s[index + 2]):
                result += 3 * convert[s[index]]
                print s[index] + s[index + 1] + s[index + 2]
                index += 3            

            elif convert[s[index]] < convert[s[index + 1]]:
                # case that there's subtraction upfront
                # 
                
                if (s[index] == 'V') or (s[index] == 'L') or (s[index] == 'D'):
                    # cannot be this way
                    return -1
                
                result += convert[s[index + 1]] - convert[s[index]]
                print s[index] + s[index + 1]
                index += 2

            else:
                # case that only reads one character
                result += convert[s[index]]
                print s[index] + ':' + str(convert[s[index]])
                index += 1
            print result

        # deal with the 2 extra char
        # 
        if index + 1 < len(s):
            if convert[s[index]] < convert[s[index + 1]]:
                # case that there's subtraction upfront
                
                if (s[index] == 'V') or (s[index] == 'L') or (s[index] == 'D'):
                    # cannot be this way
                    return -1

                result += convert[s[index + 1]] - convert[s[index]]

            else:
                # case that only reads one character
                result += convert[s[index]]
                result += convert[s[index + 1]]
        elif index < len(s):
            result += convert[s[index]]


        return result

if __name__ == '__main__':
    print Solution().romanToInt('CCCXIII')
