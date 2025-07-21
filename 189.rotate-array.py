#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ########## SOL 1 ##########
        # values = {}

        # for index, num in enumerate(nums):
        #     values[index] = num

        # for value in values:
        #     next_place = value + k

        #     if next_place > len(nums) - 1:
        #         next_place = next_place % len(nums)
            
        #     nums[next_place] = values[value]


        ########## SOL 2 ##########
        # k = k % len(nums)
        # nums[:] = nums[-k:] + nums[:-k]
        
# @lc code=end

solution = Solution()
nums = [1,2,3,4,5,6,7]
solution.rotate(nums, 2)
print(nums)



