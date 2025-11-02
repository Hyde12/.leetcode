#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (54.62%)
# Likes:    10478
# Dislikes: 470
# Total Accepted:    1M
# Total Submissions: 1.9M
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,2,3]
# Output: [3]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1]
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2]
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# Follow up: Could you solve the problem in linear time and in O(1) space?
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        majority = []
        majority_len = len(nums) // 3
        for num, count in num_count.items():
            if count > majority_len:
                majority.append(num)
                
        return majority
# @lc code=end

