import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()



def main():
    order = 'none'

    while order != "off":
        order = input("What would you like? (small/ medium/ large/ off/ report)")
        if order == "off":
            print("Have a great day")
        elif order == "report":
            print(f"Bread: {resources['bread']} slices")
            print(f"Ham: {resources['ham']} slices")
            print(f"Cheese: {resources['cheese']} ounces")
        elif order in recipes:
            if not SandwichMaker(recipes[order]["ingredients"]):
                print("Sorry there is not enough resources")
            elif SandwichMaker(recipes[order]["ingredients"]):
                print("That will be $", recipes[order]["cost"])
                coins = Cashier.process_coins(Cashier)
                if Cashier.transaction_result(Cashier,coins, recipes[order]["cost"]):
                   SandwichMaker.make_sandwich(sandwich_maker_instance,order, recipes[order]["ingredients"])
                   print("Here is your", order, "sandwich. Enjoy!")
                else:
                   print("Sorry that's not enough money. Money refunded.")
        else:print("Sorry that response was not recognized. ")


if __name__ == "__main__":
    main()
