def caching_fibonacci():
    cache = {}    # Створюємо порожній словник для зберігання обчислень

# Створюємо функцію, яка буде обчисляти числа Фібоначчі
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        # Обчислення чисел Фібоначчі
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]

    return fibonacci


fib = caching_fibonacci()  # Присвоюємо зміній fib значення функції caching_fibonacci
print(fib(10))
