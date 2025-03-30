from prices import PRICING_TABLE

class Pizza:
    def __init__(self, name, toppings, size):
        self.name = name
        self.toppings = [t.strip() for t in toppings]
        self.size = size   



    def get_price(self, prices=PRICING_TABLE):
        base = prices["base"][self.size]
        toppings = sum(
            prices["toppings"][t.strip()][self.size]
            for t in self.toppings if t in prices["toppings"]
        )
        return base + toppings