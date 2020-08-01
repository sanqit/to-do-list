class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        self.id = f"{name[0]}{last_name}{birth_year}"


print(Student(input(), input(), int(input())).id)
