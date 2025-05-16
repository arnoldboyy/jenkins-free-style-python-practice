import sys

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

if __name__ == "__main__":
    name = "KEVIN" 

    if len(sys.argv) != 2:
        print(f"Hola {name}, debes usar el script así:")
        print("Uso: python3 fahrenheit_to_celsius.py <temperatura_en_fahrenheit>")
        sys.exit(1)

    try:
        fahrenheit = float(sys.argv[1])
    except ValueError:
        print(f"{name}, por favor proporciona un número válido para la temperatura en Fahrenheit.")
        sys.exit(1)

    celsius = fahrenheit_to_celsius(fahrenheit)

    print(f"{name}, {fahrenheit} grados Fahrenheit equivalen a {celsius:.2f} grados Celsius.")


