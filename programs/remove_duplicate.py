# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if not n:
            return 0
        temp = [i for i in range(0, n)]
        j = 0

        for i in range(0, n-1):
            if nums[i] != nums[i+1]:
                temp[j] = nums[i]
                j += 1
                
        temp[j] = nums[n-1]
        j += 1

        for i in range(0, j):
            nums[i] = temp[i]

        return j

s = Solution()
res = s.removeDuplicates([])
print(res)