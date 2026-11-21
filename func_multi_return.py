def calculate(a, b):
    return a + b, a - b, a * b


add, sub, mul = calculate(10, 3)
print(f'和={add},差={sub},积={mul}')
