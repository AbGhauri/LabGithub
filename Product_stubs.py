class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      pass

  def make_purchase(self, quantity):
     try: 
        # if user entered less than 0 
        if quantity < 0 :
           raise  ValueError ("Number of items cannot be negative ")
        # if the quantity exceeds the available stock 
        if quantity > self.amount :
           raise ValueError("Not Enough Stock")
        # Deduct the amount purchased 
        self.amount -= quantity

        print("Purchase completed!")
        
     except ValueError as e :
             print ("Error : {e}")
      

# create product object
# make purchases against different product quantities (make sure to run each test case)
# do not forget to handle exceptions
# print the remaining stock after each purchases