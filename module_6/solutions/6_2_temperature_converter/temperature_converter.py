# temperature_converter.py

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    choice = input("Convert from (C)elsius or (F)ahrenheit? ").strip().upper()

    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("Invalid choice. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
