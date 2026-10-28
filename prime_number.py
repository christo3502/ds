"""Check whether a given number is prime using a loop."""

number = int(input("Enter a number: "))

if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")