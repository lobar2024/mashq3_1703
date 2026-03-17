#3
class BankCard:
    bank_name = 'AgroBank'

    def __init__(self, card_number, balance):
        self.card_number = card_number
        self.balance = balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            return 'pul yetarli emas'

    @classmethod
    def change_bank_name(cls, new_name):
        cls.change_bank_name = new_name

    @staticmethod
    def is_valid_card_number(number):
        return len(str(number)) == 16
