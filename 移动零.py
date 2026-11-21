from typing import List


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1


if __name__ == '__main__':
    solution = Solution()
    nums1 = [0, 1, 0, 3, 12]
    print(f'输入：{nums1}')
    solution.moveZeroes(nums1)
    print(f'输出：{nums1}')
    nums2 = [0]
    print(f'输入：{nums2}')
    solution.moveZeroes(nums1)
    print(f'输出：{nums2}')
    nums3 = [0, 0, 1]
    print(f'输入：{nums3}')
    solution.moveZeroes(nums3)
    print(f'输出：{nums3}')
