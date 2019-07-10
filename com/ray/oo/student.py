class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('study', (self.name, course_name))

    def paly(self):
        if self.age < 18:
            print('未成年')
        else:
            print('可以看')


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def bar(self):
        print(self.__foo)
        print('__bar')


def main():
    stu = Student('ray', 18)
    stu.study('english')
    stu.paly()
    test = Test('hello')
    # print(test.__foo)
    print(test.bar())


if __name__ == '__main__':
    main()
