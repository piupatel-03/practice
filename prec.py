class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("hello, my name is " + self.name)

p1 = person("jhon", 36)

p1.greet()



