def find_the_parent(child_type):
    parent_type = next((x for x in [Drinks, Pastry, Sweets] if issubclass(child_type, x)), None)
    if parent_type is not None:
        print(parent_type.__name__)

