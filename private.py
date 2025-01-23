class Example:
    def __init__(self):
        self.__private_attr = "I am private"

    def __private_method(self):
        return "This is a private method"

    def access_private(self):
        return self.__private_method()

# Accessing private members
obj = Example()
print(obj.access_private()) 

# print(obj.__private_attr)  #error
# print(obj.__private_method())  # error

# accesing using name mangling
print(obj._Example__private_attr)
print(obj._Example__private_method()) 

