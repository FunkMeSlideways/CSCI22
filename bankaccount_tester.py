from bankaccount import *
#imports everything from bankaccount py file

b1 = BankAccount('Alice', 8000)
b2 = BankAccount('Bob', 5000)


print(b1.account_name) # 'Alice'
print(b2.account_name) # 'Bob'
b2.account_name = 'Bobby' # Will no longer cause an error
print(b2.account_name) # 'Bobby
b2.balance = 1000000 # Will error since we did not define
                     # a balance setter

print(b2.balance)

