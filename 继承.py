class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print('%s说：我%d岁了。' % (self.name, self.age))

class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print('%s说，我%d岁了，正在读%s年级'%(self.name,self.age,self.grade))
s=student('小明',10,30,3)
s.speak()