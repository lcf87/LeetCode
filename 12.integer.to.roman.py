class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # rules of roman numbers: 
        # 1     I
        # 5     V
        # 10    X
        # 50    L
        # 100   C
        # 500   D
        # 1000  M
        # 
        # anything goes before a bigger number is NOT a multiple of 5
        # 
        # Strategy: intervals 
        # 
        # 1, 4, 9, 39, 89, 400, 900
        # 
        result = ''

        x = num

        thousand = x / 1000
        x -= thousand * 1000
        result += thousand * 'M'
        # now x is in the hundred zone
        # say x = 387 and 988 
        if (x >= 900):
            result += 'CM'
            x -= 900

        elif (x >= 500):
            result += 'D'
            x -= 500
        elif (x >= 400):
            result += 'CD'
            x -= 400
        
        hundred = x / 100
        x -= hundred * 100
        result += hundred * 'C'

        # now x in the tens zone
        if (x >= 90): 
            result += 'XC'
            x -= 90
        elif (x >= 50):
            result += 'L'
            x -= 50
        elif (x >= 40):
            result += 'XL'
            x -= 40

        ten = x / 10
        x -= ten * 10
        result += ten * 'X'


        # now x in the ones zone
        if (x == 9): 
            result += 'IX'
            x -= 9
        elif (x >= 5):
            result += 'V'
            x -= 5
        elif (x == 4):
            result += 'IV'
            x -= 4
        
        result += x * 'I'

        return result

if __name__ == '__main__':
    print Solution().intToRoman(900)
