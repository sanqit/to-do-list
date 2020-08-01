def morning(func):
    def wrapper(name):
        func(name)
        print(f"Good morning, {name}")
    return wrapper
