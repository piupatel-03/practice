
import csv
from datetime import datetime
class ExpenseTracker:
    def __init__(self, filename='expenses.csv'):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                self.expenses = [row for row in reader]
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open(self.filename, mode='w', newline='') as file:
            fieldnames = ['date', 'category', 'amount', 'description']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)

    def add_expense(self, date, category, amount, description):
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()
    def total_expenses(self):
        return sum(float(expense['amount']) for expense in self.expenses)
    def average_expense(self):
        if not self.expenses:
            return 0
        return self.total_expenses() / len(self.expenses)
    def highest_expense(self):
        if not self.expenses:
            return None
        return max(self.expenses, key=lambda x: float(x['amount']))
if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.add_expense(datetime.now().strftime('%Y-%m-%d'), 'Food', '15.50', 'Lunch')
    tracker.add_expense(datetime.now().strftime('%Y-%m-%d'), 'Transport', '7.00', 'Bus fare')
    print(f"Total Expenses: ${tracker.total_expenses():.2f}")
    print(f"Average Expense: ${tracker.average_expense():.2f}")
    highest = tracker.highest_expense()
    if highest:
        print(f"Highest Expense: ${highest['amount']} on {highest['date']} for {highest['description']}")

        
