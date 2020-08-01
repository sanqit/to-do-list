def price_string(func):
    def wrapper(arg):
        return f"£{func(arg)}"

    return wrapper  


@price_string
def new_price(amount):
    return amount * 0.9
