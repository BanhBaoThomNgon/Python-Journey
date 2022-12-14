import csv

class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # run validations to the received arguments
        assert price >= 0, f"Price {price} must be greater than or equal to zero!"
        assert quantity >= 0, f"quantity {quantity} must be greater than or equal to zero!"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # adds to the all list
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = float(item.get('quantity')),
            )

    def __repr__(self):
        return f"Item('{self.name}' : '{self.price}' : '{self.quantity}')"



# for instance in Item.all:
#     print(instance.name, instance.price)

Item.instantiate_from_csv()
print(Item.all)