import random

secret = random.randint(1, 100)
while True:
    try:
        guess = int(input('猜一个1到100的数字：'))
    except ValueError:
        print('请输入有效数字')
        continue
    if guess > secret:
        print('大了')
    elif guess < secret:
        print('小了')
    else:
        print('恭喜你，猜对了')
        break
