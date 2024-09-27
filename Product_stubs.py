class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
        # sp23-bai-003
        try:
            if quantity <= 0:
                raise ValueError("Number to be bought must be a positive integer.")
            
            # Calculate the discount
            discount = 0
            if quantity < 10:
                pass 
            elif 10 <= quantity < 99:
                discount = 10  # 10% discount
            else:
                discount = 20  # 20% discount

            # Calculate final price 
            price = (100 - discount) / 100 * self.price
            return price * quantity

        except ValueError as e:
            print(f"Error occurred: {e}")
            return None  
#sp23-bai-002
  def make_purchase(self, quantity):
      pass

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchase