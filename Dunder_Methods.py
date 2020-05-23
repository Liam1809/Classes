# Dunder Methods I
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

# Dunder Methods II
class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers

  def __iter__(self):
    return iter(self.lawyers)
  # .__len__() method that will return the number of lawyers in the law firm.
  def __len__(self):
    return len(self.lawyers)
  #  .__contains__() method that takes two parameters: self and lawyer and checks to see if lawyer is in self.lawyers.
  def __contains__(self, lawyer):
    return lawyer in self.lawyers

# instance    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

for lawyer in d_and_p:
  print(lawyer)
# print "Donelli" and "Paderewski"
print(len(d_and_p))
# print 2

if "Donelli" or "Paderewski" in d_and_p:
  print("This lawyer exists")
else:
  print("unknown lawyer")
  
# Remember that UserGroup isn’t a list, but that it contains a list.
#  These dunder methods allow us to use len for example, directly on the class and it will return the length of the list that UserGroup contains (in this case the list of users). 
# Without a dunder method, len(usergroup) would result in an error. 
  
# The __contains__() method should always either return the values True or False to indicate whether the object “contains” the item being checked.
#  How the class implements that check is dependent on the data contained in the class.
#  However, the method should always return either True or False. 
# If the method returns any other value, Python will try to convert or interpret the value as True or False and the resulting behavior may be unexpected.