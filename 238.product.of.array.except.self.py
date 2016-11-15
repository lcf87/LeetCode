class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

        Solve it without division and in O(n).

        For example, given [1,2,3,4], return [24,12,8,6].
        """

        # 1, O(n) time, O(n) space -> could convert to O(1) if if the extra space is on the back of the list...
        # idea is to accumulate the result first
        up = []
        down = []
        
        length = len(nums)
        for i in range(length):
            up.append(1)
            down.append(1)
        
        for i in range(1, length):
            up[i] = up[i-1] * nums[i-1]   

        for i in range(length-2, -1, -1):
            print i
            down[i] = down[i+1] * nums[i+1]

        for i in range(len(nums)):
          # print i
          nums[i] = up[i] * down[i]

        print up
        print down

        return nums
if __name__ == '__main__':
    print Solution().productExceptSelf([1,2,3,4,5,6,7,8])
