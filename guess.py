age = 20
print(age >= 18)
print(age == 18)
print(age != 18)

secret = 7
guess = int(input('猜一个1到10数字'))

if guess > secret:
    print('大了')
elif guess < secret:
    print('小了')
else:
    print('猜对了！')

import random

secret = random.randint(1, 100)

while True:
    guess = int(input('猜一个1到100的数字：'))
    if guess > secret:
        print('大了')
    elif guess < secret:
        print('小了')
    else:
        print('恭喜你，猜对了！')
        break
