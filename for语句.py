sites = ['baidu', 'google', 'runbook', 'table']
for site in sites:
    print(site)

word = 'runoob'
for letter in word:
    print(letter)

for number in range(1, 6):
    print(number)

# for...else
for x in range(6):
    print(x)
else:
    print('Finally finished!')

sites = ['daidu', 'google', 'runoob', 'taobao']
for site in sites:
    if site == 'runoob':
        print('菜鸟教程')
        break
    print('循环数据' + site)
else:
    print('没有循环数据')
print('完成循环！')
