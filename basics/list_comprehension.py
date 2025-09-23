# List Comprehension
numbers = [i * i for i in range(5)]
print(numbers)  # [0, 1, 4, 9, 16]

even_squares = [i * i for i in range(10) if i % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]