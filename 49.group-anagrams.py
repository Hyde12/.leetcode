#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from collections import defaultdict 

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # O (m * n), where m is the # of strings and n is the longest string
        anagrams = defaultdict(list)

        for string in strs:
            letter_count = [0] * 26

            for letter in string:
                letter_count[ord(letter) - ord("a")] += 1

            anagrams[tuple(letter_count)].append(string)
        
        return list(anagrams.values())
# @lc code=end

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
