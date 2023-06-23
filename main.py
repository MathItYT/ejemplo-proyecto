"""Programa para hallar los números primos en un rango.

Ejemplo
-------
    $ python main.py file.txt 1 10
    2
    3
    5
    7
    La salida ha sido escrita a file.txt
"""

import sys

filename, start, stop = sys.argv[1:]
start, stop = int(start), int(stop)

def prime_numbers(start: int, stop: int) -> list[int]:
    """Hallar los números primos en un rango.

    Parameters
    ----------
        start : int
            Número inicial del rango.
        stop : int
            Número final del rango.

    Returns
    -------
        list[int]
            Lista de números primos en el rango.
    """
    primes = []
    for number in range(start, stop + 1):
        if number > 1:
            for divisor in range(2, number):
                if number % divisor == 0:
                    break
            else:
                primes.append(number)
    return primes


def main():
    """Función principal del programa."""
    prime_numbers_list = prime_numbers(start, stop)
    with open(filename, "w") as file:
        for number in prime_numbers_list:
            print(number)
            print(number, file=file)

    print(f"La salida ha sido escrita a {filename}")

if __name__ == "__main__":
    main()
