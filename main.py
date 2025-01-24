MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def checking_ingredients(order_ingredients):
    for materials in order_ingredients:
        if order_ingredients[materials] >= resources[materials]:
            print("Sorry there is not enough water.")
            return False
    return True

def checking_amount(user_amount, drink_cost):
    if user_amount >= drink_cost:
        change = round(user_amount - drink_cost,2)
        print(f"the amount change is {change}")
        global profit
        profit +=drink_cost
        return True
    else:
        print("the amount is not enough")
        return  False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}  Enjoy!")

coffee = True
while coffee:
    user_choice = input("What would you like? (espresso/latte/cappuccino) and you also want to see resources please click 'R' please click off for shutdown \n").lower()
    if user_choice =="off":
        coffee = False
        print("see you later")
    elif user_choice== "r":
        print(f"water:{resources["water"]}")
        print(f"milk:{resources["milk"]}")
        print(f"coffee:{resources["coffee"]}")
    else:
        drink = MENU[user_choice]
        if checking_ingredients(drink["ingredients"]):
            payment = process_coins()
            if checking_amount(payment,drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])





