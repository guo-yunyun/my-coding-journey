try:
    age = int(input('请输入你的年龄：'))
    print(f'明年你就{age + 1}岁了')
except ValueError:
    print('输入的不是有效数字，请重新运行试试')
print('-' * 20)
try:
    number = int(input('请输入数字：'))
    result = 10 / number
    print(f'10除以{number}等于{result}')
except ValueError:
    print('输入的不是数字')
except ZeroDivisionError:
    print('不能除以0')
# 抓获所有异常
# try:
#     ...
# except Exception as e:
#     print(f'出错了：{e}')
print('-' * 20)
try:
    age = int(input('请输入年龄：'))
except ValueError:
    print('输入的不是数字')
else:
    print(f'明年你就{age + 1}岁了')
print('-' * 20)
try:
    f = open('note.txt', 'r', encoding='utf-8')
    content = f.read()
    print(content)
except FileNotFoundError:
    print('文件不存在')
finally:
    print('这句话总会出现')
print('-' * 20)


def set_age(age):
    if age < 0 or age > 150:
        raise ValueError('年龄必须在0到150之间')#主动抛出异常
    print(f'年龄设置为{age}')


set_age(100)
