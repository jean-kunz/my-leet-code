#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        answer =[i,j]
                        return answer
        return answer
# @lc code=end
assert Solution().twoSum([2,1,4,12,5],14)==[0,3]
assert Solution().twoSum([3,3],6)==[0,1]


