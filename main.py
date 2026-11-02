
from users import registrera_anvandare
from database import visa_bocker, lana_bok, mina_lan, alla_lan

user_id = None

while True:
    print("Bibliotek")
    print("1. Registrera användare")
    print("2. Visa tillgängliga böcker")
    print("3. Låna bok")
    print("4. Mina lånade böcker")
    print("5. Bibliotekets utlånade böcker")
    print("6. Avsluta")

    val = input("Välj ett alternativ: ")

    if val == "1":
        user_id = registrera_anvandare()

    elif val == "2":
        visa_bocker()

    elif val == "3":
        if user_id is not None:
            lana_bok(user_id)
        else:
            print("Du måste registrera dig först.")

    elif val == "4":
        if user_id is not None:
            mina_lan(user_id)
        else:
            print("Du måste registrera dig först.")

    elif val == "5":
        alla_lan()

    elif val == "6":
        print("Programmet avslutas.")
        break

    else:
        print("Ogiltigt val, försök igen.")
