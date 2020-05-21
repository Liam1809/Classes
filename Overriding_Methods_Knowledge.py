# Overriding Methods
# Inheritance is a useful way of creating objects with different class variables, but is that all it’s good for? What if one of the methods needs to be implemented differently? In Python, all we have to do to override a method definition is to offer a new definition for the method in our subclass.

# An overridden method is one that has a different definition from its parent class. What if User class didn’t have an is_admin flag but just checked if it had permission for something based on a permissions dictionary? It could look like this:

# class User:
#   def __init__(self, username, permissions):
#     self.username = username
#     self.permissions = permissions

#   def has_permission_for(self, key):
#     if self.permissions.get(key):
#       return True
#     else:
#       return False
# Above we defined a class User which takes a permissions parameter in its constructor. Let’s assume permissions is a dict. User has a method .has_permission_for() implemented, where it checks to see if a given key is in its permissions dictionary. We could then define our Admin user like this:

# class Admin(User):
#   def has_permission_for(self, key):
#     return True
# Here we define an Admin class that subclasses User. It has all methods, attributes, and functionality that User has. However, if you call has_permission_for on an instance of Admin, it won’t check its permissions dictionary. Since this User is also an Admin, we just say they have permission to see everything!

# class A(object):
#     def do_something(self, parm1):
#         print("A - do_something - was passed " + str(parm1))

# class B(A):
#     def do_something(self, parm1):
#         # Works for both Python 2 and 3
#         A.do_something(self, parm1 + 1)

#         # Python 2 - this only works if A inherits from object
#         # super(B, self).do_something(parm1 + 1)

#         # Python 3 -
#         # super().do_something(parm1 + 1)
#         print("B - do_something - was passed " + str(parm1))


# obj = B()

# obj.do_something(100)

#OUTPUTS:
# A - do_something - was passed 101
# B - do_something - was passed 100


# Super()
# Overriding methods is really useful in some cases but sometimes we want to add some extra logic to the existing method. In order to do that we need a way to call the method from the parent class. Python gives us a way to do that using super().

# super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s parent class (also called its superclass). We call the required function as a method on super():

# class Sink:
#   def __init__(self, basin, nozzle):
#     self.basin = basin
#     self.nozzle = nozzle

# class KitchenSink(Sink):
#   def __init__(self, basin, nozzle, trash_compactor=None):
#     super().__init__(basin, nozzle)
#     if trash_compactor:
#       self.trash_compactor = trash_compactor
# Above we defined two classes. First, we defined a Sink class with a constructor that assigns a rinse basin and a sink nozzle to a Sink instance. Afterwards, we defined a KitchenSink class that inherits from Sink. KitchenSink‘s constructor takes an additional parameter, a trash_compactor. KitchenSink then calls the constructor for Sink with the basin and nozzle it received using the super() function, with this line of code:

# super().__init__(basin, nozzle)
# This line says: “call the constructor (the function called __init__) of the class that is this class’s parent class.” In the example given, KitchenSink‘s constructor calls the constructor for Sink. In this way, we can override a parent class’s method to add some new functionality (like adding a trash_compactor to a sink), while still retaining the behavior of the original constructor (like setting the basin and nozzle as instance variables).