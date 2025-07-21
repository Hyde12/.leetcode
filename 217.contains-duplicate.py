#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_count = set()

        for num in nums:
            if num in num_count:
                return True

            num_count.add(num)
        
        return False
# @lc code=end

