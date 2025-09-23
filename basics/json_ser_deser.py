# W Pythonie do pracy z JSON-em używa się wbudowanego modułu json.
#
# Serializacja → konwersja słownika (lub innej struktury Python) do JSON-a.
#
# Deserializacja → konwersja JSON-a do słownika Pythona.

import json

# Przykładowy słownik
person = {
    "name": "Jan",
    "age": 30,
    "city": "Warszawa"
}

# --- SERIALIZACJA: słownik → JSON ---
person_json = json.dumps(person)  # tworzy string JSON
print(person_json)
# {"name": "Jan", "age": 30, "city": "Warszawa"}

# --- DESERIALIZACJA: JSON → słownik ---
person_dict = json.loads(person_json)
print(person_dict)
# {'name': 'Jan', 'age': 30, 'city': 'Warszawa'}

# Możemy teraz odwoływać się jak do słownika
print(person_dict["name"])  # Jan


# Wyjaśnienia
#
# json.dumps(obj) → zamienia obiekt Pythona (dict, list, etc.) na string JSON.
#
# json.loads(json_string) → zamienia string JSON na obiekt Pythona (np. słownik).
#
# Jeśli chcesz zapisać JSON bezpośrednio do pliku → użyj json.dump(obj, file) i json.load(file).