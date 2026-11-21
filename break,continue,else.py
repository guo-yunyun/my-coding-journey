n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')

for letter in 'runoob':
    if letter == 'b':
        break
    print('当前字母为：', letter)

var = 10
while var > 0:
    print('当前变量值为：', var)
    var = var - 1
    if var == 5:
        break
print('Good bye!')

for letter in 'runoob':
    if letter == 'o':
        continue
    print('当前字母：', letter)

var = 10
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('当前变量值：', var)
print('Good bye!')

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n // x)
            break
    else:
        print(n, '是质数')

# pass语句
for letter in 'runoob':
    if letter == 'o':
        pass
        print('执行pass模块')
    print('当前字母：', letter)
print('Good bye!')
