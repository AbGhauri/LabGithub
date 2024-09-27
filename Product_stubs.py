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
      

product = Product("Laptop", 10, 1000)

# Test Cases

# case 1: purchasing 3 items
product.make_purchase(3)
print("Remaining stock: {product.amount}")

# case 2: purchasing 5 items
product.make_purchase(5)
print("Remaining stock: {product.amount}")

# case 3: purchasing 2 items
product.make_purchase(2)
print("Remaining stock: {product.amount}")

# case 4: more than available stock 
product.make_purchase(1) 
# This should fail, since the stock is 0 now
print("Remaining stock: {product.amount}")

# case 5: negative items
product.make_purchase(-3)
print("Remaining stock: {product.amount}")
