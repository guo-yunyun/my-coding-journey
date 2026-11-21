# 方法一
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        检查字符串是否可以由其子串重复多次构成
        方法：字符串拼接+包含判断
        """
        return s in (s + s)[1:-1]


if __name__ == '__main__':
    solution = Solution()
    s1 = 'abab'
    print(f'输入：s={s1},输出：{solution.repeatedSubstringPattern(s1)}')
    s2 = 'aba'
    print(f'输入：s={s2},输出：{solution.repeatedSubstringPattern(s2)}')
    s3 = 'abcabcabc'
    print(f'输入：s={s3},输出：{solution.repeatedSubstringPattern(s3)}')

print()


# 方法2枚举法
class Solution:
    def repeatedSubstringPattern(self, s) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                substring = s[:i]
                if substring * (n // i) == s:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    s1 = 'abab'
    print(f'输入：s={s1},输出：{solution.repeatedSubstringPattern(s1)}')
    s2 = 'aba'
    print(f'输入：s={s2},输出：{solution.repeatedSubstringPattern(s2)}')
    s3 = 'abcabcabc'
    print(f'输入：s={s3},输出：{solution.repeatedSubstringPattern(s3)}')

print()


# 方法3KMP算法
class Solution:
    def repeatedSubstringPattern(self, s) -> bool:
        if len(s) == 0:
            return False
        n = len(s)
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
            lps[i] = j
        max_len = lps[-1]
        min_rep_len = n - max_len
        return max_len > 0 and n % min_rep_len == 0


if __name__ == '__main__':
    solution = Solution()
    s1 = 'abab'
    print(f'输入：s={s1},输出：{solution.repeatedSubstringPattern(s1)}')
    s2 = 'aba'
    print(f'输入：s={s2},输出：{solution.repeatedSubstringPattern(s2)}')
    s3 = 'abcabcabc'
    print(f'输入：s={s3},输出：{solution.repeatedSubstringPattern(s3)}')
