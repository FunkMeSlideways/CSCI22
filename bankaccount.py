class BankAccount:
    
    def __init__(self, account_name, balance):
        self._account_name = account_name
        self._balance = balance

    @property
    def account_name(self):
        return self._account_name
    
    @account_name.setter
    def account_name(self, new_name):
        self._account_name = new_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    