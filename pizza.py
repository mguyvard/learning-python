def make_pizza(size, *toppings):
    """Create  adictionary for a pizza"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")
        