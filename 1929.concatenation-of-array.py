#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#
# https://leetcode.com/problems/concatenation-of-array/description/
#
# algorithms
# Easy (90.51%)
# Likes:    3606
# Dislikes: 423
# Total Accepted:    1M
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,1]'
#
# Given an integer array nums of length n, you want to create an array ans of
# length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n
# (0-indexed).
# 
# Specifically, ans is the concatenation of two nums arrays.
# 
# Return the array ans.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# 
# Example 2:
# 
# 
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # return nums + nums
        new_nums = [0] * (len(nums) * 2)

        for index, num in enumerate(nums):
            new_nums[index] = num
            new_nums[len(nums) + index] = num
        
        return new_nums
# @lc code=end