# Najpierw zapisujemy linię do pliku
with open("example.txt", "w") as file:
    file.write("To jest pierwsza linia\n")

# Teraz odczytujemy plik
with open("example.txt", "r") as file:
    line = file.readline()
    print("Odczytana linia:", line.strip())

# Możemy też dopisać kolejną linię
with open("example.txt", "a") as file:
    file.write("To jest dopisana linia\n")
