class ComboMeal:

    def __init__(self, main_meal, drink, side, discount_code):
        self.__main_meal = main_meal
        self.__drink = drink
        self.__side = side
        self.__discount_code = discount_code

    def show(self):
        print("----- Combo Meal -----")

        if hasattr(self.__main_meal, "describe"):
            print(f"Main Meal: {self.__main_meal.describe()}")
        else:
            print(f"Main Meal: {self.__main_meal}")

        print(f"Drink: {self.__drink}")
        print(f"Side: {self.__side}")
        print(f"Discount Code: {self.__discount_code}")


class ComboMealBuilder:

    def __init__(self):
        self.main_meal = None
        self.drink = None
        self.side = None
        self.discount_code = None

    def set_main_meal(self, main_meal):
        self.main_meal = main_meal
        return self

    def set_drink(self, drink):
        self.drink = drink
        return self

    def set_side(self, side):
        self.side = side
        return self

    def set_discount(self, discount_code):
        self.discount_code = discount_code
        return self

    def build(self):
        return ComboMeal(
            self.main_meal,
            self.drink,
            self.side,
            self.discount_code
        )
