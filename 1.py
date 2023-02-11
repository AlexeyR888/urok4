# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 75
#
# class Parent(Grandparent):
#     age = 40
#
# class Child(Parent):
#     height = 50
#
#     def __init__(self):
#         print(self.height)
#         print(self.age)
#         print(self.satiety)
#
# nick = Child()

class Hello_world:
    hello = "Hello"
    _hello = "_hello"
    __hello = "__hello"

    def __init__(self):
        self.world = "World"
        self._world = "_World"
        self.__world = "__World"

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hi(Hello_world):

    def hi_printer(self):
        print(self.hello)
        print(self._hello)
        # print(self.__hello)
        print(self.world)
        print(self._world)
        # print(self.__world)

hello = Hello_world()
hello.printer()
hi = Hi()
hi.hi_printer()