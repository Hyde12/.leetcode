#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        prev_zero = 0

        for index, num in enumerate(nums):
            if num != 0:
                nums[prev_zero], nums[index] = nums[index], nums[prev_zero]
                prev_zero += 1
# @lc code=end

solution = Solution()

nums = [1,1,3,0,12]

solution.moveZeroes(nums)
print(nums)
