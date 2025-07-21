#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer = 1
        
        for index, num in enumerate(nums):
            if num != nums[pointer - 1]:
                nums[pointer] = nums[index]
                pointer += 1

        return pointer

        
# @lc code=end
solution = Solution()

nums = [1]

unique = solution.removeDuplicates(nums)
print(f"{nums}, {unique}")


