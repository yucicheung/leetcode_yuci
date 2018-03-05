# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, nums, target):
        """
        complexity : O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, value in enumerate(nums):
            loss = target - value
            if value in dict:#如果能和之前的数配对
                return [dict[value], index]
            else:#否则记录谁能与之配对
                dict[loss] = index
        return None

# test case
s = Solution()
print s.twoSum([3,2,4],6)
print s.twoSum([3,3],6)