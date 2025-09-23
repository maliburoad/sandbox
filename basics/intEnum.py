from enum import IntEnum

class Status(IntEnum):
    NEW = 1
    IN_PROGRESS = 2
    DONE = 3

# Użycie
print(Status.NEW)        # Status.NEW
print(Status.NEW.value)  # 1

# Można porównywać jak int
if Status.DONE == 3:
    print("Zakończone!")  # ✔️
