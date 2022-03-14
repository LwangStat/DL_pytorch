#print("hello python")
ls = ['a'] * 2
print(ls)
class MyClass:
    """A simple example class"""
    i = 12345
    j = 4321

    def f(self):
        return 'hello world'

x = MyClass()
print(x.i,x.j)
y = MyClass()
y.j = 1234
print(x.i,x.j)
print(x.i,y.j)