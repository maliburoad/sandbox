# Słownik: klucz → wartość
person = {
    "name": "Jan",
    "age": 30,
    "city": "Warszawa"
}


print(person.keys())  # dict_keys(['name', 'age', 'city'])

# Jeśli chcesz w formie listy
print(list(person.keys()))  # ['name', 'age', 'city']


print(person.values())  # dict_values(['Jan', 30, 'Warszawa'])

# W formie listy
print(list(person.values()))  # ['Jan', 30, 'Warszawa']

for key, value in person.items():
    print(f"{key}: {value}")