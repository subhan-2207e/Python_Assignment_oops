class Bank:
    bank_name = "Mehzan bank"

    @classmethod

    def change_bank_name(cls , name):
        cls.bank_name = name

b1 = Bank()
print(b1.bank_name)

Bank.change_bank_name("Al Habib Bank")

print(b1.bank_name)
