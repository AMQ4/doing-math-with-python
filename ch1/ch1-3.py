def print_menu():
    print("0. to exit")
    print("1. Kilometers to Miles")
    print("2. Kilograms to Pounds")
    print("3. Celsius to Fahrenheit")
    print("-n to swap.")


def km_mi(km):
    return km / 1.609


def mi_km(mi):
    return mi * 1.609


def C_F(C):
    return C * (9/5) + 32


def F_C(F):
    return 5 * (F - 32) / 9


def kilo_pound(kilo):
    return kilo * 2.20462


def pound_kilo(p):
    return p / 2.20462


m = {0: exit, 1: km_mi, -1: mi_km, 2: kilo_pound, -2: pound_kilo, 3: C_F, -3: F_C}
while True:
    print_menu()
    try:
        n = int(input("Which conversion would you like to do:\n> "))
        if n not in range(-3, 4):
            raise ValueError("out of range.")
        if n == 0:
            m[n]()
        quantity = float(input("Enter the quantity you want to convert to the selected scale\n> "))

    except ValueError as e:
        print(e)
    
    else:
        print(m[n](quantity))
