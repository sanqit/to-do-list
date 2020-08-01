def tallest_people(**people):
    max_height = max(people.values())

    for name, height in sorted(people.items()):
        if height == max_height:
            print(f"{name} : {height}")
