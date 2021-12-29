"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.



Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Can you find an O(n) solution?

"""
import sys


class Solution:
    def thirdMax(self, nums: list) -> int:
        if len(set(nums)) < 3:
            return max(nums)

        first = second = third = -2147483648  # possible min value

        for val in nums:
            if val > first:
                third, second = second, first
                first = val
            elif val > second and val < first:
                third, second = second, val
            elif val > third and val < second:
                third = val
        return third


s = Solution()
nums = [2, 2, 3, 1]
print(s.thirdMax(nums))
nums = [1, 2]
print(s.thirdMax(nums))
nums = [3, 2, 1]
print(s.thirdMax(nums))
nums = [1,2,2,5,3,5]
print(s.thirdMax(nums))
