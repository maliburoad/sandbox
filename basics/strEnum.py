from enum import StrEnum

class Role(StrEnum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

# Użycie
print(Role.ADMIN)        # Role.ADMIN
print(Role.ADMIN.value)  # "admin"

# Można porównywać jak string
if Role.USER == "user":
    print("Zwykły użytkownik")  # ✔️
