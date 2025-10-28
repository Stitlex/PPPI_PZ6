def add(num1, num2):
    """Повертає суму двох чисел."""
    return num1 + num2

def percent_of(number, percent):
    """Повертає відсоток від числа."""
    return number * percent / 100

def discount(price, percent):
    """Розраховує ціну зі знижкою."""
    if percent < 0 or percent > 100:
        raise ValueError("Відсоток має бути від 0 до 100")
    return price - (price * percent / 100)


if __name__ == "__main__":
    number1 = 20
    number2 = 25
    number = 200
    percent = 15
    price = 1250

    result_sum = add(number1, number2)
    print(result_sum)

    result_percent = percent_of(number, percent)
    print(result_percent)

    result = discount(price, result_percent)
    print(result)
