#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.00%)
# Likes:    21684
# Dislikes: 1171
# Total Accepted:    2.7M
# Total Submissions: 5.7M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,0,1,2]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)

        longest_consecutive = 1
        for num in num_set:
            if num - 1 not in num_set:
                cons = num
                consecutive = 1

                while cons + 1 in num_set:
                    consecutive += 1
                
                if consecutive > longest_consecutive:
                    longest_consecutive = consecutive
        
        return longest_consecutive
# @lc code=end

