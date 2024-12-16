
hp = 100
xp = 0

def stats():
    print(f"### HP {hp} ### XP {xp} ###")

def welcome_screen():
    print("#####################")
    print("   Vítej v RPG hře   ")
    print("#####################")

    print("\nMenu:")
    print("1 - Zahájit hru")
    print("Cokoliv jiného - ukončit hru")

def tavern():
    print("---------------------")
    print("  Jsi v krčmě  ")
    print("---------------------")

    stats()

    print("\nMenu:")
    print("1 - koupím si pivo")
    print("2 - Koupím si polévku")
    print("3 - koupím si velé jídlo")

    choice = input("vyber z menu: ")
    if int(choice) == 1:
        print("koupil jsis báječné pivo")
    elif int(choice) == 2:
        print("koupil jsis hnusnou polévku")
    elif int(choice) == 3:
        print("dostal jsis před sebe divočáka")

    stats()
    crossroad()

def crossroad():
    print("---------------------")
    print("  Jsi na křižovatce  ")
    print("---------------------")

    print("\nMenu:")
    print("1 - Tréninkové hřiště")
    print("2 - Krčma")
    print("3 - Souboj")

    choice = input("vyber z menu: ")
    if int(choice) == 1:
        print("Budeš trénovat")
    elif int(choice) == 2:
        print("Půjdeš do krčmy")
        tavern()
    elif int(choice) == 3:
        print("Budeš bojovat")
    else:
        crossroad()

def main():
    welcome_screen()

    choice = input("Vyber z menu: ")
    if int(choice) == 1:
        crossroad()
    else:
        print("hra ukončena")


main()
