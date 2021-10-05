toppings = ["Bacon", "Chicken", "Pepperoni", "Cheese", "Olives", "Anchovies"]
prices = [2, 4, 1, 2, 3, 6]

num_of_2_slices = prices.count(2)
num_pizzas = len(toppings)

pizza_and_prices1 = zip(prices, toppings)
pizza_and_prices = list(pizza_and_prices1)
print(pizza_and_prices)

pizza_and_prices.sort(reverse = True)
cheapest_pizza = pizza_and_prices[-1:]
pricest_pizza = pizza_and_prices[:1]
pizza_and_prices.pop(0)
pizza_and_prices.insert(-1, (1.5, "Pineapple"))
cheapest_three = pizza_and_prices[-3:]
print(cheapest_three)