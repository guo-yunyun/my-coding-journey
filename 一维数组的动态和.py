class Solution:
    def runningSum(self,nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.runningSum(nums)
    print('输入：', nums)
    print('输出：', result)
