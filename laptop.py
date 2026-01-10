from item import Item
class Laptop(Item):
    def __init__(self, name: str, price: float, quantity=0, year=2026):
        super().__init__(name,price,quantity)
        assert 2015<=year<=2026, f"{year} is not the valid year for this"
        self.year = year