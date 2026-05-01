def add_expense_item(expenses, description, amount, category):
    new_item = {
        "description": description,
        "amount": float(amount),
        "category": category
    }
    expenses.append(new_item)
    return expenses

def calculate_total(expenses):
    return sum(item["amount"] for item in expenses)

def get_by_category(expenses, category):
    return [item for item in expenses if item["category"].lower() == category.lower()]