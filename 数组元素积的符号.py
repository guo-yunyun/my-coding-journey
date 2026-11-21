from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_count = 0
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                neg_count += 1
                return -1
        if neg_count % 2 != 0:
            return -1
        else:
            return 1


if __name__ == '__main__':
    sol = Solution()
    nums1 = [-1, -2, -3, -4, 3, 2, 1]
    result1 = sol.arraySign(nums1)
    print(f'输入：nums={nums1}')
    print(f'输出：{result1}')
    print('-' * 30)
    nums2 = [1, 5, 0, 2, -3]
    result2 = sol.arraySign(nums2)
    print(f'输入：nums={nums2}')
    print(f'输出：{result2}')
    print('-' * 30)
    nums3 = [1, 2, 3]
    print(f'输入：nums={nums3}')
    print(f'输出：{sol.arraySign(nums3)}')
