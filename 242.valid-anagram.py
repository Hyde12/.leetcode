#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = {}

        for letter in s:
            letters[letter] = letters.get(letter, 0) + 1
        
        for letter in t:
            if letter in letters:
                letters[letter] -= 1

                if letters[letter] < 0:
                    return False
            else:
                return False
        
        return True
# @lc code=end

