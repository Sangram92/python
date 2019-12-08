
# Given a non-empty array of integers, every element appears twice except for one. 
# Find that single one

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. using count method
        
        # for no in nums:
        #     if nums.count(no) == 1:
        #         return no

        # 2. Using 2 for loops

        # for idx, no in enumerate(nums):
        #     cur_no = no
        #     duplicate_found = False
        #     for idx_, no_ in enumerate(nums):
        #         if no == no_ and idx != idx_:
        #             duplicate_found = True
        #             cur_no = ""
        #     if not duplicate_found:
        #         return cur_no

        # 3. Using XOR: it returns 0 for same no 
        res = nums[0]
        for i in range(1, len(nums)):
            print(res, nums[i])
            res = res ^ nums[i]
        return res

sol = Solution()
res = sol.singleNumber([1, 7, 1])
print(res)
