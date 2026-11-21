# 列表推导式
names = ['bbbbb', 'aaaa', 'cc', 'dd']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)

# 字典推导式
listdemo = ['google', 'runoob', 'taobao']
new_dict = {key: len(key) for key in listdemo}
print(new_dict)

dic = {x: x ** 2 for x in (2, 4, 6)}
print(dic)
print(type(dic))

# 集合推导式
setnew = {i ** 2 for i in (1, 2, 3)}
print(setnew)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print(type(a))

# 元组推导式
a = (x for x in range(1, 10))
print(a)
print(tuple(a))
