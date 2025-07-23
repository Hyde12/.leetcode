#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (79.87%)
# Likes:    9087
# Dislikes: 1201
# Total Accepted:    3.3M
# Total Submissions: 4.1M
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters s.
# 
# You must do this by modifying the input array in-place with O(1) extra
# memory.
# 
# 
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.
# 
# 
#

# @lc code=start
class Solution:
    def reverseString(self, s: list[str]) -> None:
        r = len(s) - 1

        for l in range(len(s)):
            if l >= r:
                return

            s[l], s[r] = s[r], s[l]
            r -= 1
        
# @lc code=end

