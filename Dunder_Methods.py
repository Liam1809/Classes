# Dunder Methods
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

class Atom:
  def __init__(self, label):
    self.label = label
  # return string representation also pass it to object of Molecule class, that means 
  # atoms in Molecule holds a list [This is Na,This is Cl]
  def __repr__(self):
    return "This is {atom}".format(atom = self.label)
    # return self.label
  
  def __add__(self, other):
    return Molecule([self, other])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
  def __repr__(self):
    # return str(self.atoms)
    combined_molecule = ""
    for index in range(len(self.atoms)):
      # uncomment to check the diff
      # combined_molecule += str(self.atoms[index]) + " " 
      combined_molecule += self.atoms[index].label
    return combined_molecule
      
# instances
sodium = Atom("Na")
chlorine = Atom("Cl")
print(sodium)
print(chlorine)
# salt = Molecule([sodium, chlorine])
# meaning salt = Molecule([sodium, chlorine
salt = sodium + chlorine
print(salt)

# The __add__() method can be implemented to return whatever type or class makes sense for the operation.
#  For this exercise, the addition of two Atom objects returns a Molecule. 
# In some other case, a class may just return a new instance of the same class. 
# The __add__() method is free to return whatever makes sense for the operation being performed.