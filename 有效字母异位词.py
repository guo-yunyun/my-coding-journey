class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        record = [0] * 26
        for i in s:
            record[ord(i) - ord('a')] += 1
        for i in t:
            record[ord(i) - ord('a')] -= 1
        for i in record:
            if i != 0:
                return False
        return True


if __name__ == '__main__':
    my_tool = Solution()
    s_test = 'anagram'
    t_test = 'nagaram'
    result = my_tool.isAnagram(s_test, t_test)
    print('测试结果：', result)
