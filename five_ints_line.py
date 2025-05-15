#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: april, 2025
# The program
def main():
    # this function prints numbers from 1000 to 2000, five per line
    for number in range(1000, 2001):
        print(number, end=" ")
        if (number - 999) % 5 == 0:
            print()


if __name__ == "__main__":
    main()
