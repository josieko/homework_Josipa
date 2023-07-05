class NoFundsError(Exception):
    pass


class MaxTriedError(Exception):
    pass


def sim_shop():

    # like the sims game since it's a SIMulation shop (pun intended)
    cakes = {
        "Red velvet cheesecake": 60,
        "Blood orange, dark chocolate and olive oil cake": 80,
        # this cake sounds weird but it's actually one of my favourites to make (and eat of course),
        # here's the recipe hehe https://tasty.co/recipe/blood-orange-chocolate-olive-oil-cake
        "Pistachio dream": 85,
        "Vegan mango cheesecake": 120
    }
    available_budget = 100
    attempts = 0
    adding_money_attempts = 0

    try:
        print("Well hello there! Welcome to Josie's cake shop!")
        print("Here's what we have today: ")
        for item, price in cakes.items():
            print(f"{item}: £{price}")

        while True:
            option = input("Tell me which cake you want to order ('exit' to leave the shop): ")
            if option == "exit":
                break

            try:
                cake_price = cakes[option]
                if cake_price > available_budget:
                    raise NoFundsError
                else:
                    available_budget -= cake_price
                    print(f"Here's your {option}!")
                    print("Thank you for choosing us! Let us know how we did 🧁")
                    attempts += 1

            except KeyError:
                raise ValueError("Sorry, we don't sell that cake. Please try again next time.")

            except NoFundsError:
                print("Sorry for the inconvenience but your funds are insufficient.")
                if adding_money_attempts < 3:
                    mo_money = input("Do you have more money to add to your account? (yes/no): ")
                    if mo_money.lower() == "yes":
                        adding_money = float(input("Enter the amount you wish to add: £"))
                        available_budget += adding_money
                        adding_money_attempts += 1
                        continue
                    else:
                        break
                else:
                    if available_budget < min(cakes.values()):
                        raise MaxTriedError
                    else:
                        attempts = 0
                        adding_money_attempts = 0
                        break
            if attempts == 3:
                if available_budget < min(cakes.values()):
                    raise MaxTriedError
                else:
                    attempts = 0
                    adding_money_attempts = 0

    except MaxTriedError:
        print("Sorry, you reached the maximum number of attempts. You can come back another time!")

    except ValueError as e:
        print(str(e))

    finally:
        print("Thank you for choosing Josie's cake shop! See you another time 🧁")


sim_shop()
