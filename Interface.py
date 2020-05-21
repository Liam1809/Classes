class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * 0.001

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return self.price_of_insured_item * 0.00005

# Implementing the same Interface
def price(vehicle_or_home):
  return vehicle_or_home.get_rate()

# instances 
vehicle = VehicleInsurance(10)
home = HomeInsurance(100)

for item in [vehicle, home]:
  print(price(item))
  
# If the signature of the method is changed then it is not implementing the interface. 
# The methods must share the same name and attributes to be considered as implementing the interface.