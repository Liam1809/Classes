# print(dir(list))
class SortedList(list):
  def __init__(self, lst):
    # initialise the internal state of the object with the passed in list argument.This is done with the super method.
    super().__init__(lst)
    self.sort()
  def append(self, value):
    super().append(value)
    self.sort()
  def extend(self, value):
    super().extend(value)
    self.sort()
# instantialise SortedList with original list [7,5,3,1]
lst = SortedList([7,5,3,1])
# original list
print("Original sorted List:" + str(lst))
# print [] because we are not creating a new list with the value that was passed in. To do this, we need to call the list class’s __init__ method to initialise the internal state of the object with the passed in list argument. This is done with the super method.
# uncomment super().__init__(lst)
# lst object applies append method
lst.append(8)
lst.append(1)
lst.append(7)
lst.append(5)
lst.append(-4)
print("Appended sorted List: " + str(lst))
# lst object applies extend method
lst.extend([1,10,3,5])
print("extended sorted List: " + str(lst))

# print(dir(dict))
class NewDict(dict):
  fallback = 'No such a key found!'

  def __init__(self, values):
    # initialise the internal state of the object with the passed in dict argument.This is done with the super method. 
    super().__init__(values)

  def __getitem__(self, key):
    try:
      return super().__getitem__(key)
    except KeyError:
      return self.fallback
      

nd = NewDict({"a": 1, "b": 2, "c": 3})

print(nd["e"])
print(nd["a"])

for key, value in nd.items():
  print("key : {key}\nvalue : {value}".format(key = key, value = value))