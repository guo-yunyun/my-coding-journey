class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = sum(ord(char) for char in t) - sum(ord(char) for char in s)
        return chr(diff)


if __name__=='__main__':
    solution=Solution()
    s='abcd'
    t='abcde'
    result=solution.findTheDifference(s,t)
    print(f'字符串s:{s}')
    print(f'字符串t:{t}')
    print(f'被添加的字母是:{result}')

