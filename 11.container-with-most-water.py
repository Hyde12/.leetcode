#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (57.95%)
# Likes:    31753
# Dislikes: 2037
# Total Accepted:    4.3M
# Total Submissions: 7.3M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_volume = 0

        while l < r:
            max_height = l if height[l] < height[r] else r
            width = r - l 
            volume = height[max_height] * width

            if volume > max_volume:
                max_volume = volume
            
            if max_height == l:
                l += 1
            else:
                r -= 1
            
        return max_volume
# @lc code=end

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
