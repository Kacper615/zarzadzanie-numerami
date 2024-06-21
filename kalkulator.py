def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def mnoz(a, b):
    return a * b

def dziel(a, b):
    if b != 0:
        return a / b
    else:
        return "Dzielenie przez zero!"

def menu():
    print("Wybierz operację:")
    print("1. Dodaj")
    print("2. Odejmij")
    print("3. Mnoż")
    print("4. Dziel")
    print("5. Zakończ")

if __name__ == "__main__":
    while True:
        menu()
        wybor = input("Wybierz opcję (1/2/3/4/5): ")
        
        if wybor == '5':
            print("Koniec programu")
            break
        
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))
        
        if wybor == '1':
            print(f"Wynik: {dodaj(num1, num2)}")
        elif wybor == '2':
            print(f"Wynik: {odejmij(num1, num2)}")
        elif wybor == '3':
            print(f"Wynik: {mnoz(num1, num2)}")
        elif wybor == '4':
            print(f"Wynik: {dziel(num1, num2)}")
        else:
            print("Nieprawidłowy wybór")
