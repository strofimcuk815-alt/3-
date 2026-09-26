class Ingredient:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class Food:
    def __init__(self, name, ingredients):
        self.name = name

        self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def show_recipe(self):
        print(f"Страва: {self.name}")
        print("Інгредієнти:")
        for ingr in self.ingredients:
            print(f" - {ingr.name}")

cheese = Ingredient("Сир")
tomato = Ingredient("Томати")
dough = Ingredient("Тісто")
meat = Ingredient("Котлета")

pizza = Food("Піца", [dough, tomato, cheese])
burger = Food("Бургер", [dough])

burger.add_ingredient(meat)
burger.add_ingredient(cheese)
burger.add_ingredient(tomato)

pizza.show_recipe()
burger.show_recipe()

