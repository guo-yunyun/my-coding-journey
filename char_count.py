text = input('请输入一段文字：')
count = {}
for char in text:
    count[char] = count.get(char, 0) + 1
    print(f'处理字符{char}后，字典变成：{count}')
print('\n最终结果:')
for char, times in count.items():
    print(f'{char}出现了{times}次')
