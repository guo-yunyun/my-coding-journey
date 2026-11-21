try:
    a = float(input('被除数：'))
    b = float(input('除数：'))
    result = a / b
except ValueError:
    print('请输入有效数字')
except ZeroDivisionError:
    print('除数不能为0')
else:
    print(f'结果是{result}')
