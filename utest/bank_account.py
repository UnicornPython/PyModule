
import requests

class BankAccount:

    def __init__(self, init_balance):
        if init_balance < 0:
            raise ValueError("Initial balance cannot be negetive")
        self.balance = init_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negetive")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdraw amount cannot be negetive")
        self.balance -= amount

    def get_interest_rate(self):
        url = "https://api.example.com/interest_rate"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("rate")
        else:
            raise Exception("Failed to fetch interest rate")

