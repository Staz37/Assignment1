class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: "))
        halfdollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickles = int(input("how many nickles?: "))
        total = quarters * 0.25 + dollars * 1 + nickles * 0.05 + halfdollars * .5
        return total
        ###

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            return False
        ##

