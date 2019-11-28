# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print("input ...........", nums, k)
        if k > 0:
            for i in range(0, k):
                temp = nums.pop()
                nums.insert(0, temp)

        print("nums.............", nums)

solobj = Solution()
solobj.rotate([1,2,3,4], 2) 