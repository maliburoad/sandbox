try:
    x = int(input("Podaj liczbę: "))
    y = int(input("Podaj dzielnik: "))
    result = x / y
    print("Wynik:", result)

# Łapanie dwóch konkretnych wyjątków
except ValueError:
    print("To nie jest poprawna liczba!")
except ZeroDivisionError:
    print("Nie można dzielić przez zero!")

# Ogólny wyjątek na wszystkie pozostałe błędy
except Exception as e:
    print("Wystąpił inny błąd:", e)

# Blok finally zawsze się wykona
finally:
    print("Koniec programu")


# Wyjaśnienia
#
# try → miejsce, w którym może wystąpić wyjątek.
#
# except ValueError: → łapie konkretny typ wyjątku.
#
# except ZeroDivisionError: → łapie drugi konkretny typ.
#
# except Exception as e: → złapie wszystkie inne wyjątki i zapisze je w zmiennej e.
#
# finally: → wykona się zawsze, niezależnie od tego, czy wyjątek wystąpił, czy nie.