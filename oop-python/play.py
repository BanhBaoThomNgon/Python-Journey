class Inventory():
    allProducts = []
    discount = 0.7
    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        Inventory.allProducts.append(self)
    
    def sales(self):
        return self.price * self.quantity
        

object1 = Inventory('laptop', 1000, 476)

object2 = Inventory('Iphone', 1200, 245)

object3 = Inventory('macbook', 1000, 58)

object4 = Inventory('tablet', 599, 50)