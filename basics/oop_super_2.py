

# jeśli użyjesz super(), to przy tworzeniu obiektu w klasie potomnej faktycznie zostanie odpalony __init__ zarówno w klasie dziecka, jak i w klasie rodzica.


class A:
    def __init__(self):
        print("Init A")

class B(A):
    def __init__(self):
        super().__init__()   # wywołuje __init__ z A
        print("Init B")

obj = B()
