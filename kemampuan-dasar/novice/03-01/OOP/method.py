class Person:
    pass  # An empty block

p = Person()
print(p)

class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
