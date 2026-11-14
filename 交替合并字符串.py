
class Solution:
    def mergeAIternately(self,word1:str,word2:str)->str:
        res = []
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
             if i < len(word1):
                res.append(word1[i])
                i += 1
             if j < len(word2):
                res.append(word2[j])
                j += 1
        return "".join(res)
#测试1
# if __name__ == '__main__':
#     solution = Solution()
#     w1 = "hello"
#     w2 = "world"
#     result=solution.mergeAIternately(w1,w2)
#     print(f'输入word1:{w1},word2:{w2}')
#     print(f'合并后的结果为{result}')
#进阶测试
if __name__ == '__main__':
    solution = Solution()
    word1 = input('请输入第一个字符串{word1}：')
    word2 = input('请输入第二个字符串{word2}：')
    result = solution.mergeAIternately(word1,word2)
    print('合并后的结果是：',result)



