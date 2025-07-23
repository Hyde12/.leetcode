#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[r].isalnum():
                r -= 1
            elif not s[l].isalnum():
                l += 1
            else:
                left_letter = s[l].lower()
                right_letter = s[r].lower()

                if left_letter != right_letter:
                    return False
                
                r -= 1
                l += 1

        return True
# @lc code=end

