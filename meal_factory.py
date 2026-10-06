from abc import ABC, abstractmethod


class Meal(ABC):

    @abstractmethod
    def describe(self):
        pass


class Pizza(Meal):

    def describe(self):
        return "Pizza is made with dough, sauce, cheese, and toppings."


class Burger(Meal):

    def describe(self):
        return "A burger contains a patty served inside a bun."


class Salad(Meal):

    def describe(self):
        return "A salad is made with fresh vegetables and other ingredients."


class MealFactory:

    @staticmethod
    def create_meal(meal_type: str):

        meal_type = meal_type.lower()

        if meal_type == "pizza":
            return Pizza()

        elif meal_type == "burger":
            return Burger()

        elif meal_type == "salad":
            return Salad()

        else:
            return None
