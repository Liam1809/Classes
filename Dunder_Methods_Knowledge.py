# Dunder Methods I
# One way that we can introduce polymorphism to our class definitions is by using Python’s special dunder methods. We’ve explored a few already, the constructor __init__ and the string representation method __repr__, but that’s only scratching the tip of the iceberg.

# Python gives us the power to define dunder methods that define a custom-made class to look and behave like a Python builtin. What does that mean? Say we had a class that has an addition method:

# class Color:
#   def __init__(self, red, blue, green):
#     self.red = red
#     self.blue = blue
#     self.green = green

#   def __repr__(self):
#     return "Color with RGB = ({red}, {blue}, {green})".format(red=self.red, blue=self.blue, green=self.green)

#   def add(self, other):
#     """
#     Adds two RGB colors together
#     Maximum value is 255
#     """
#     new_red = min(self.red + other.red, 255)
#     new_blue = min(self.blue + other.blue, 255)
#     new_green = min(self.green + other.green, 255)

#     return Color(new_red, new_blue, new_green)

# red = Color(255, 0, 0)
# blue = Color(0, 255, 0)

# magenta = red.add(blue)
# print(magenta)
# # Prints "Color with RGB = (255, 255, 0)"
# In this code we defined a Color class that implements an addition function. Unfortunately, red.add(blue) is a little verbose for something that we have an intuitive symbol for (i.e., the + symbol). Well, Python offers the dunder method __add__ for this very reason! If we rename the add() method above to something that looks like this:

# class Color: 
#   def __add__(self, other):
#     """
#     Adds two RGB colors together
#     Maximum value is 255
#     """
#     new_red = min(self.red + other.red, 255)
#     new_blue = min(self.blue + other.blue, 255)
#     new_green = min(self.green + other.green, 255)

#     return Color(new_red, new_blue, new_green)
# Then, if we create the colors:

# red = Color(255, 0, 0)
# blue = Color(0, 255, 0)
# green = Color(0, 0, 255)
# We can add them together using the + operator!

# # Color with RGB: (255, 255, 0)
# magenta = red + blue

# # Color with RGB: (0, 255, 255)
# cyan = blue + green

# # Color with RGB: (255, 0, 255)
# yellow = red + green

# # Color with RGB: (255, 255, 255)
# white = red + blue + green
# Since we defined an __add__ method for our Color class, we were able to add these objects together using the + operator.

# Dunder Methods II
# Python offers a whole suite of magic methods a class can implement that will allow us to use the same syntax as Python’s built-in data types. You can write functionality that allows custom defined types to behave like lists:

# class UserGroup:
#   def __init__(self, users, permissions):
#     self.user_list = users
#     self.permissions = permissions

#   def __iter__(self):
#     return iter(self.user_list)

#   def __len__(self):
#     return len(self.user_list)

#   def __contains__(self, user):
#     return user in self.user_list
# In our UserGroup class above we defined three methods:

# __init__, our constructor, which sets a list of users to the instance variable self.user_list and sets the group’s permissions when we create a new UserGroup.
# __iter__, the iterator, we use the iter() function to turn the list self.user_list into an iterator so we can use for user in user_group syntax. For more information on iterators, review Python’s documentation of Iterator Types.
# __len__, the length method, so when we call len(user_group) it will return the length of the underlying self.user_list list.
# __contains__, the check for containment, allows us to use user in user_group syntax to check if a User exists in the user_list we have.
# These methods allow UserGroup to act like a list using syntax Python programmers will already be familiar with. If all you need is something to act like a list you could absolutely have used a list, but if you want to bundle some other information (like a group’s permissions, for instance) having syntax that allows for list-like operations can be very powerful.

# We would be able to use the following code to do this, for example:

# class User:
#   def __init__(self, username):
#     self.username = username

# diana = User('diana')
# frank = User('frank')
# jenn = User('jenn')

# can_edit = UserGroup([diana, frank], {'can_edit_page': True})
# can_delete = UserGroup([diana, jenn], {'can_delete_posts': True})

# print(len(can_edit))
# # Prints 2

# for user in can_edit:
#   print(user.username)
# # Prints "diana" and "frank"

# if frank in can_delete:
#   print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")
# Above we created a set of users and then added them to UserGroups with specific permissions. Then we used Python built-in functions and syntax to calculate the length of a UserGroup, to iterate through a UserGroup and to check for a User‘s membership in a UserGroup.