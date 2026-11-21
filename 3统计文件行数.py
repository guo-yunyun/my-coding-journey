with open('diary.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(f'共{len(lines)}行')
print(f'共{sum(len(line) for line in lines)}个字符')
