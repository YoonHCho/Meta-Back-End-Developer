class Recipe:
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print(
            f"The {self.dish} has {str(self.items)} and takes {str(self.time)} minutes to prepare")


newDish = Recipe('Sandwich', ['bread', 'meat', 'lettuce'], 5)
pizza = Recipe('dough', ['sauce', 'cheese'], 30)
newDish.contents()
pizza.contents()
