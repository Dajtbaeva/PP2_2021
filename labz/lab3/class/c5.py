class Account:
    def __init__(self, own, balance):
        self.own = own
        self.balance = balance

    def deposit(self, income):
        self.income = income
        self.balance += self.income
        print(f'Вы успешно пополнили ваш счет на сумму {self.income}\nВаш текущий счет: {self.balance}')

    def withdraw(self, snyali):
        self.snyali = snyali
        if self.balance >= self.snyali:
            self.balance -= self.snyali
            print(f'Вы успешно сняли {self.snyali}\nВаш текущий баланс: {self.balance}')
        else:
            print(f'Недостаточно средств\nВаш текущий баланс: {self.balance}')


A1 = Account(input('Введите ваше имя\n'), int(input()))
A1.deposit(int(input('Вставьте купюру в купюроприемник\n')))
A1.withdraw(int(input('Введите нужную вам сумму\n')))
