class JustCouter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCouter()
counter.count()
counter.count()
print(counter.publicCount)


# print(counter.__secerCount)#报错
class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name:', self.name)
        print('url:', self.__url)

    def __foo(self):
        print('这是私有方法')

    def foo(self):
        print('这是公有方法')
        self.__foo()


x = Site('随便一个名', '随便一个网址')
x.who()
x.foo()
# x.__foo()#报错
# x._Site__foo()#可以，需先注释掉32行

