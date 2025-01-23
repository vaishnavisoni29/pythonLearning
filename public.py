class Example:
    def __init__(self):
        self.public_attr = "I am public"

    def public_method(self):
        return "This is a public method"

obj = Example()
print(obj.public_attr)      
print(obj.public_method()) 
