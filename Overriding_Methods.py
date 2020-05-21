# Overriding Methods
class Message:
      def __init__(self, sender, recipient, text):
          self.sender = sender
          self.recipient = recipient
          self.text = text
    
class User:
  def __init__(self, username):
    self.username = username
    
  # message in here is an instance of Message class  
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

class Admin(User):
  def edit_message(self, message, new_text):
    message.text = new_text
    
    
# super()
class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions
  def __repr__(self):
    return "This is the original recipient"


class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40
  
# ingredient = PotatoSalad(3, 4, 5)
# print(dir(ingredient))
# print(ingredient.potatoes)
# print(ingredient.celery)
# print(ingredient.onions)

ingredient1 = SpecialPotatoSalad(3, 4, 5)
print(ingredient1)

print(dir(ingredient1))
print(ingredient1.potatoes)
print(ingredient1.celery)
print(ingredient1.onions)
print(ingredient1.raisins)

#  an inherited class is not required to call the __init__() method of the parent class. 
#  If no __init__() method is implemented in the inherited class, then the parent __init__() will be called automatically when an object of the inherited class is created. 
#  If __init__() is implemented in the inherited class, then that will override the parent class method.
#   The parent class method will NOT be called unless the call is written in the inherited class.