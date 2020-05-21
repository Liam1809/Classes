
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))
print(len(a_dict))
print(len(a_string))

#  The len() function will attempt to call a method named __len__() on your class. 
# This is one of the special methods known as a “dunder method” (for double underscore) which Python will look for to perform special operations.
#  Implementing that method will allow the len() call to work on the class. 
#  If it is not implemented, the call to len() will fail with an AttributeError.
#  The following code example shows a class implementing __len__().

class Bag:
    def __init__(self, item_count):
        self.item_count = item_count

    def __len__(self):
        return self.item_count


mybag = Bag(10)

print(len(mybag))

# OUTPUTS: 10