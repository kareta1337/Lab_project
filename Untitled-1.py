def fibonacci(n):
    """
    Функція fibonacci повертає n-те число Фібоначчі.
    """
    if n < 0:
        raise ValueError("n повинно бути невід'ємним.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Введіть номер числа Фібоначчі: "))
result = fibonacci(n)
print("Число Фібоначчі під номером", n, "дорівнює", result)
