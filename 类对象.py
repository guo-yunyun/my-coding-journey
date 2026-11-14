class MyClass:
    """一个简单实例"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()
print('MyClass类的属性i:', x.i)
print('MyClass类的方法输出为:', x.f())


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


class Object:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)


obj = Object(42)
obj.display_value()
