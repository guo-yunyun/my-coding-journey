from typing import List


class Solution:
    def plusOne(self, digits: list[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == '__main__':
    sol = Solution()
    test_case = [[1, 2, 3], [4, 3, 2, 1], [9, 9, 9], [1, 9, 9], [0]]
    for digits in test_case:
        result = sol.plusOne(digits.copy())
        print(f'输入：{digits},加一后的结果：{result}')
