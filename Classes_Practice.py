# Methods with Arguments
class Circle:
  pi = 3.14
  def area(self, radius):
    return self.pi * radius ** 2

# instance
circle = Circle()

pizza_area = circle.area(12//2)
teaching_table_area = circle.area(36//2)
round_room_area = circle.area(11460/2)
# print(pizza_area)
# print(teaching_table_area)
# print(round_room_area)

# Constructor
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {}".format(diameter))
  
teaching_table = Circle(36)

# Instance Variables
class Store:
      pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

print(alternative_rocks.store_name)

# Attribute Functions
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element)
    print(element.count("s"))
    
# self
class Circle:
      # class variable
  pi = 3.14
  # constructor
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2
  # string representation 
  def __repr__(self):
        return "Circle with radius {radius}".format(radius = self.radius)
    # method
  def circumference(self):
    return 2 * self.pi * self.radius

# instances
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# instances access method
print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())
