from item import Item
class Phone(Item):
    def __init__(self,name:str,price:int,quantity=0,broken_phone=0):
        super().__init__(name,price,quantity)
        assert broken_phone >= 0, f" broken phone {broken_phone} must be greater than or eq"
        self.broken_phone = broken_phone

    @staticmethod
    def about_this_class():
        return f"Phone is a child class. It inherit from Item class."

