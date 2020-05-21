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


class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40
# ingredient = PotatoSalad("potato", "salad", "carrot")
# print(dir(ingredient))
# print(ingredient.potatoes)
# print(ingredient.celery)
# print(ingredient.onions)

ingredient1 = SpecialPotatoSalad("potato", "salad", "carrot")
print(dir(ingredient1))
print(ingredient1.potatoes)
print(ingredient1.celery)
print(ingredient1.onions)
print(ingredient1.raisins)