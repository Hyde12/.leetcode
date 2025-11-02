#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#
# https://leetcode.com/problems/merge-strings-alternately/description/
#
# algorithms
# Easy (82.22%)
# Likes:    4748
# Dislikes: 139
# Total Accepted:    1.9M
# Total Submissions: 2.3M
# Testcase Example:  '"abc"\n"pqr"'
#
# You are given two strings word1 and word2. Merge the strings by adding
# letters in alternating order, starting with word1. If a string is longer than
# the other, append the additional letters onto the end of the merged string.
# 
# Return the merged string.
# 
# 
# Example 1:
# 
# 
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# 
# 
# Example 2:
# 
# 
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# 
# 
# Example 3:
# 
# 
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.
# 
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # word1_len = len(word1)
        # word2_len = len(word2)

        # if word1_len < word2_len:
        #      loop_len = word1_len
        #      end_str = word2[loop_len:]
        # else:
        #     loop_len = word2_len
        #     end_str = word1[loop_len:]
        
        # i = 0
        # new_str = ""
        # while i < loop_len:
        #     new_str += word1[i] + word2[i]
        #     i += 1

        # return new_str + end_str

        ### Two Pointer Approach
        word1_len = len(word1)
        word2_len = len(word2)
        count_1, count_2 = 0, 0
        new_str = ""

        while (count_1 < word1_len or count_2 < word2_len):
            if count_1 < word1_len:
                new_str += word1[count_1]
                count_1 += 1
            
            if count_2 < word2_len:
                new_str += word2[count_2]
                count_2 += 1
        
        return new_str
# @lc code=end


