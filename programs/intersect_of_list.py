class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int] [1,2,2,1]
        :type nums2: List[int] [2,2]
        :rtype: List[int]
        """
        intersect_list = []
        for n1 in nums1:
            if n1 in nums2:
                if n1 in intersect_list:
                    num_count = intersect_list.count(n1) + 1
                    if num_count == 1 or (num_count <= nums1.count(n1) and num_count <= nums2.count(n1)):
                        intersect_list.append(n1)
                else:
                    intersect_list.append(n1)
        return intersect_list