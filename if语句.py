var1 = 100
if var1:
    print('1-if表达式条件为True')
    print(var1)
var2 = 0
if var2:
    print('2-if表达式条件为Ture')
    print(var2)
print('Good bye!')

age = int(input('请输入你家狗狗的年龄：'))
print('')
if age <= 0:
    print('你是在逗我吧')
elif age == 1:
    print('相当一个14岁的人')
elif age == 2:
    print('相当一个22岁的人')
elif age > 2:
    human = 22 + (age - 2) * 5
    print('对应人类的年龄：', human)
input('点击enter键退出')
