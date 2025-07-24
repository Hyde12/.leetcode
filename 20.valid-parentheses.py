#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (42.48%)
# Likes:    26153
# Dislikes: 1909
# Total Accepted:    6.3M
# Total Submissions: 14.8M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "()[]{}"
# 
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: s = "(]"
# 
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: s = "([])"
# 
# Output: true
# 
# 
# Example 5:
# 
# 
# Input: s = "([)]"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            elif char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                parentheses = stack.pop()

                if (parentheses != '(' and char == ')') or (parentheses != '[' and char == ']') or (parentheses != '{' and char == '}'):
                    return False

        return len(stack) == 0     
# @lc code=end

