class Person:
    def __init__(self, name):
        self._name = name  # prywatne pole (konwencja _)

    # getter
    @property
    def name(self):
        return self._name

    # setter
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

# Użycie
p = Person("Jan")
print(p.name)  # getter → "Jan"

p.name = "Adam"  # setter
print(p.name)  # "Adam"

# Próba ustawienia pustej nazwy
# p.name = ""  # ValueError: Name cannot be empty
