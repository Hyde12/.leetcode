#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (65.36%)
# Likes:    34554
# Dislikes: 618
# Total Accepted:    2.9M
# Total Submissions: 4.5M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        l_wall = 0
        r_wall = 1
        spaces = []

        max_water = 0

        while r_wall < len(height):
            width = r_wall - l_wall - 1
            if height[l_wall] == 0:
                spaces = []
                l_wall += 1
                r_wall += 1
            elif height[r_wall] == 0 or width == 0:
                spaces.append(height[r_wall])
                r_wall += 1
            else:
                max_height = height[l_wall] if height[l_wall] < height[r_wall] else r_wall

                for space in spaces:
                    max_water += max_height - space
            
            if height[r_wall] >= height[l_wall]:
                spaces = []
                l_wall = r_wall
                r_wall = l_wall + 1

        return max_water
        
# @lc code=end

solution = Solution()
print(solution.trap([0,2,0,3,1,0,1,3,2,1]))