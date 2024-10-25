def main():
    print("Enter a temperature: ")
    fahrenheit  = float(input())
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"The temperature in fahrenheit is {fahrenheit:.2f}")
    print(f"The temperature in celsius is {celsius:.2f}")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

main()