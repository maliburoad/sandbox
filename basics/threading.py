import threading
import time

# Funkcja, którą będziemy uruchamiać w wątku
def greet(name):
    for i in range(3):
        print(f"Cześć, {name}!")
        time.sleep(1)

# Tworzymy wątek
thread = threading.Thread(target=greet, args=("Jan",))

# Uruchamiamy wątek
thread.start()

# Możemy robić coś w głównym wątku równolegle
for i in range(3):
    print("Główny wątek działa...")
    time.sleep(1)

# Czekamy, aż wątek zakończy działanie
thread.join()
print("Wątek zakończony!")


# Wyjaśnienia
#
# threading.Thread(target=..., args=...) → tworzy wątek, który wykona podaną funkcję z argumentami.
#
# thread.start() → uruchamia wątek.
#
# thread.join() → czeka aż wątek zakończy działanie, zanim program pójdzie dalej.