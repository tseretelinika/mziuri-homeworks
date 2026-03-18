class Ticket:
    def __init__(self, film_name, ticket_value, ticket_amount, language = "geo"):
        self.film_name = film_name
        self.ticket_value = ticket_value
        self.ticket_amount = ticket_amount
        self.language = language

    def __str__(self):
        return f"ფილმის სახელია {self.film_name}"

    def __le__(self, other, quantity):
        if self.ticket_amount <= other.ticket_amount:
            print("true")
        else:
            print("false")
        if other.ticket_amount <= quantity:
            print(f"{other.ticket_amount} is less or equal then {quantity}")
        else:
            print(f"{other.ticket_amount} is more than {quantity}")



class User:
    def __init__(self, buyer_name, balance):
        self.buyer_name = buyer_name
        self.balance = balance

    def __str__(self):
        return f"მყიდველის სახელია {self.buyer_name} და მისი ბალანსი უდრის:{self.balance}"

    def deposit(self, amount):
        if amount <= 0:
            print("რიცხვი დადებითი უნდა იყოს რომ დაემატოს ბალანსს")
        else:
            self.balance += amount

    def buy_ticket(self, ticket, amount):
        if self.balance >= amount and self.ticket_value >= amount:
            self.balance -= ticket.ticket_value * amount
            ticket.ticket_value -= amount
            print(f"you bought {amount} tickets")
        elif ticket.ticket_value * amount > self.balance:
            print("not enough balance")
        else:
            print("not enought ticket left")



