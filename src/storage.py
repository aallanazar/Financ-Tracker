import json
import os

FILENAME = "expenses.json"

def load_expenses():
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_expenses(expenses):
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Fehler beim Speichern: {e}")
