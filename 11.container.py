class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        length = len(height)

        i = 0
        j = length - 1

        max_vol = 0
        vol = 0
        step = 0

        while i < j:

            vol = (length - 1 - step) * min(height[i], height[j])
            print vol

            if vol > max_vol:
                max_vol = vol

            # decide which side to move
            left_vol = min(height[i + 1], height[j]) * (length - 2 - step)
            right_vol = min(height[j - 1], height[i]) * (length - 2 - step)
            curr_vol = vol

            if curr_vol > left_vol and curr_vol > right_vol:
                # current is hte largest
                # compare the hight
                if (height[i] < height[j]):
                    i += 1
                else:
                    j -= 1
            else:
                # current is not the highest
                if left_vol < right_vol:
                    j -= 1
                elif left_vol > right_vol:
                    i += 1
                else:
                    if (height[i] < height[j]):
                        i += 1
                    else:
                        j -= 1


            step += 1
        return max_vol





def main():

	print Solution().maxArea([1,2])

if __name__ == '__main__':
	main()