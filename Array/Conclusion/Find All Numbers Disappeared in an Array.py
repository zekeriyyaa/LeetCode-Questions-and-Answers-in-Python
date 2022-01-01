"""
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n


Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

"""


class Solution:
    def findDisappearedNumbers(self, nums: list) -> list:

        index = 0
        while index < len(nums):
            if nums[index] == "*":
                index += 1
            else:
                if nums[nums[index]-1]=="*":
                    index+=1
                else:
                    temp = nums[index]
                    nums[index] = nums[nums[index]-1]
                    nums[temp-1] = "*"
        return list(i+1 for i in range(len(nums)) if nums[i] != "*")

s = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(s.findDisappearedNumbers(nums))
nums = [1, 1]
print(s.findDisappearedNumbers(nums))
