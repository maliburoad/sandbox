from dataclasses import dataclass

# dataclass to fajny sposób w Pythonie, żeby szybko tworzyć klasy przechowujące dane – bez pisania dużo kodu „boilerplate” (__init__, __repr__, itp.).
#
# automatyczne __init__ (nie musisz pisać konstruktora),
# automatyczne __repr__ (ładne printowanie obiektów),
# automatyczne __eq__ (porównywanie obiektów po polach).
#
#


@dataclass
class User:
    id: int
    name: str
    email: str

# Tworzymy obiekt
user = User(id=1, name="Jan Kowalski", email="jan.kowalski@example.com")

# Automatycznie działa __repr__, więc łatwo wypisać:
print(user)
# User(id=1, name='Jan Kowalski', email='jan.kowalski@example.com')

# Dostęp do pól
print(user.name)  # Jan Kowalski