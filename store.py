#store.py

#
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        if not card_number.isdigit() or len(card_number) != 16:
            raise ValueError("Invalid credit card number. Must be 16 digits.")
        self.card_number = card_number

    def pay(self, amount):
        print(f"Charging credit card {self.card_number} for ${amount}")

class Paypal(PaymentMethod):
    def __init__(self, email):
        if "@" not in email:
            raise ValueError("Invalid PayPal email.")
        self.email = email

    def pay(self, amount):
        print(f"Processing PayPal payment for ${amount} from {self.email}")


class BitcoinPayment(PaymentMethod):
    def __init__(self, wallet_address):
        if not wallet_address.startswith("btc_"):
            raise ValueError("Invalid Bitcoin wallet address.")
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"Processing Bitcoin payment of ${amount} from wallet {self.wallet_address}")


class Order:
    def __init__(self, amount):
        if amount <= 0:
            raise ValueError('Amount must be greater than zero')
        self.amount = amount

    def process_payment(self, payment_method: PaymentMethod):
        payment_method.pay(self.amount)

try:
    order = Order(150)

    cc = CreditCard("1234567812345678")  # Valid 16-digit number
    order.process_payment(cc)

    print("---")

    pp = Paypal("customer@example.com")  # Valid email
    order.process_payment(pp)

    print("---")

    bitcoin = BitcoinPayment("btc_123abc456def")
    order.process_payment(bitcoin)  # Should work with no changes to Order ✅

except ValueError as e:
    print("Validation error:", e)
