import os

NUMERY_FILE = "numery.txt"

def load_numery():
    if os.path.exists(NUMERY_FILE):
        with open(NUMERY_FILE, 'r') as file:
            numery = [int(line.strip()) for line in file]
    else:
        numery = []
    return numery

def save_numery(numery):
    with open(NUMERY_FILE, 'w') as file:
        for numer in numery:
            file.write(f"{numer}\n")

def add_numer(numer):
    numery = load_numery()
    numery.append(numer)
    save_numery(numery)

def list_numery():
    numery = load_numery()
    print("Numery w liście:")
    for numer in numery:
        print(numer)

def sort_numery():
    numery = load_numery()
    numery.sort()
    save_numery(numery)
    print("Numery posortowane pomyślnie.")

def main():
    while True:
        print("\n1. Wyświetl numery")
        print("2. Dodaj numer")
        print("3. Posortuj numery")
        print("4. Wyjdź")
        choice = input("Wybierz opcję: ")
        
        if choice == '1':
            list_numery()
        elif choice == '2':
            numer = int(input("Podaj numer do dodania: "))
            add_numer(numer)
        elif choice == '3':
            sort_numery()
        elif choice == '4':
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()