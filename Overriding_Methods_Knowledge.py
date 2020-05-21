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