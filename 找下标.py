class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


if __name__ == '__main__':
    solution = Solution()
    result1 = solution.strStr('sadbutsad', 'sad')
    print('测试一的结果是', result1)
    result2 = solution.strStr('apple', 'apl')
    print('测试二的结果是', result2)
