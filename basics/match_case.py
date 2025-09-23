def day_type(day: str) -> str:
    match day:
        case "poniedziałek" | "wtorek" | "środa" | "czwartek" | "piątek":
            return "Dzień roboczy"
        case "sobota" | "niedziela":
            return "Weekend"
        case _:
            return "Nieznany dzień"

print(day_type("poniedziałek"))  # Dzień roboczy
print(day_type("sobota"))        # Weekend
print(day_type("xyz"))           # Nieznany dzień