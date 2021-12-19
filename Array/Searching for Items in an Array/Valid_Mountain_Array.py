"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Input: arr = [2,1]
Output: false

Input: arr = [3,5,5]
Output: false

Input: arr = [0,3,2,1]
Output: true

"""


class Solution:
    def validMountainArray(self, arr: list) -> bool:
        if len(arr)<3:
            return False

        top=False
        for i in range(len(arr)-1):
            if not top:
                if arr[i]<arr[i+1] and i!=len(arr)-2:
                    continue
                elif arr[i]>arr[i+1] and i!=0:
                    top = True
                else:
                    return False
            else:
                if arr[i]>arr[i+1]:
                    continue
                else:
                    return False
        return True


arr = [0,3,2,1]
arr1 = [2,1]
arr2 = [3,5,5]
s = Solution()
print(s.validMountainArray(arr))
print(s.validMountainArray(arr1))
print(s.validMountainArray(arr2))




