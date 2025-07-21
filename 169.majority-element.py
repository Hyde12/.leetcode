#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Boyer-Moore Majority Algorithm
        candidate = nums[0]
        votes = 0

        for i in nums:
            if candidate == i:
                votes += 1
            else:
                votes -= 1

            if votes == 0:
                candidate = i
                votes = 1

        return candidate
# @lc code=end

solution = Solution()

nums = [3,2,3]

print(solution.majorityElement(nums))
