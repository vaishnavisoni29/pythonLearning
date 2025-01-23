class Example:
    def __init__(self):
        self._protected_attr = "I am protected"

    def _protected_method(self):
        return "This is a protected method"

class SubExample(Example):
    def access_protected(self):
        return self._protected_method()
    
# accessed using subclass
sub_obj = SubExample()
print(sub_obj.access_protected())
#accessed directly
print(sub_obj._protected_attr)
