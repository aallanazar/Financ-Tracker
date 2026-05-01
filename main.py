from storage import load_expenses, save_expenses
from logic import add_expense_item, calculate_total

def main():
    expenses = load_expenses()
    
    while True:
        print("\n--- MEIN FINANZ-TRACKER ---")
        print("1. Ausgabe hinzufügen")
        print("2. Alle Ausgaben anzeigen")
        print("3. Gesamtbilanz zeigen")
        print("4. Beenden & Speichern")
        
        choice = input("Wähle eine Option (1-4): ")
        
        if choice == "1":
            desc = input("Was hast du gekauft? ")
            try:
                amt = float(input("Wie viel hat es gekostet? "))
                cat = input("Kategorie (z.B. Essen, Fahrt, Abo): ")
                expenses = add_expense_item(expenses, desc, amt, cat)
                print("Erfolgreich hinzugefügt!")
            except ValueError:
                print("Fehler: Bitte gib eine gültige Zahl für den Betrag ein.")
                
        elif choice == "2":
            print("\nDeine Ausgaben:")
            for i, item in enumerate(expenses, 1):
                print(f"{i}. {item['description']}: {item['amount']}€ ({item['category']})")
                
        elif choice == "3":
            total = calculate_total(expenses)
            print(f"\nGesamtausgaben: {total:.2f}€")
            
        elif choice == "4":
            save_expenses(expenses)
            print("Daten gespeichert. Bis bald!")
            break
        else:
            print("Ungültige Wahl, versuch es nochmal.")

if __name__ == "__main__":
    main()