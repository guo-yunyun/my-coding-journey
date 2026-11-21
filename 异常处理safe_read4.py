filename = input('文件名:')
try:
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('文件不存在')
